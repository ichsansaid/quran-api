import uvicorn

from infra.fastapi.app import NewFastAPIApp
from infra.fastapi.handlers.get_daftar_surah_handler import GetDaftarSurahHandler
from infra.fastapi.handlers.get_detail_ayat_surah_handler import GetDetailAyatSurahHandler
from infra.fastapi.handlers.get_detail_tafsir_surah_handler import GetDetailTafsirSurahHandler
from infra.fastapi.routers.surah_router import SurahRouter

app = NewFastAPIApp(
    routers=[
        SurahRouter(
            get_daftar_surah_handler=GetDaftarSurahHandler(),
            get_detail_ayat_surah_handler=GetDetailAyatSurahHandler(),
            get_detail_tafsir_surah_handler=GetDetailTafsirSurahHandler()
        )
    ]
)
uvicorn.run(
    app,
    host='0.0.0.0',
    port=8000,
    log_level="info"
)
