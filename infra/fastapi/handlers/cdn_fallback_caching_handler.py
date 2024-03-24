import os

import urllib3
from starlette.exceptions import HTTPException
from starlette.staticfiles import StaticFiles
from starlette.types import Scope, Receive, Send


class CdnFallbackCachingHandler(StaticFiles):
    def __init__(self, directory: str, fallback_caching_url: str):
        super().__init__(directory=directory)
        self.fallback_caching_url = fallback_caching_url
        self.http = urllib3.PoolManager()

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        assert scope["type"] == "http"

        if not self.config_checked:
            await self.check_config()
            self.config_checked = True

        path = self.get_path(scope)
        try:
            response = await self.get_response(path, scope)
            await response(scope, receive, send)
        except HTTPException as ex:
            if ex.status_code == 404:
                repath = path.replace(os.path.sep, "/")
                url = f"{self.fallback_caching_url}{repath}"
                response = self.http.request("get", url)
                if response.status == 200:
                    dirs = path.split(os.path.sep)
                    dirs.pop()
                    for i in range(len(dirs)):
                        if not os.path.exists(os.path.join(self.directory, *dirs[:i+1])):
                            os.mkdir(os.path.join(self.directory, *dirs[:i+1]))
                    with open(os.path.join(self.directory, path), "wb") as f:
                        f.write(response.data)
                    response = await self.get_response(path, scope)
                    await response(scope, receive, send)
            raise ex
