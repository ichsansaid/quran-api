from typing import Dict, List, Callable

from fastapi import FastAPI, APIRouter


class NewFastAPIApp:
    def __init__(self, routers: List[Callable[[], APIRouter]]):
        self.routers = routers

    def __call__(self) -> FastAPI:
        app = FastAPI()
        for router in self.routers:
            app.include_router(router())
        return app
