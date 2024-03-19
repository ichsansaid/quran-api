import uvicorn

from infra.fastapi.app import NewFastAPIApp
from infra.fastapi.handlers.get_daftar_surah_handler import GetDaftarSurahHandler
from infra.fastapi.handlers.get_detail_ayat_surah_handler import GetDetailAyatSurahHandler
from infra.fastapi.handlers.get_detail_tafsir_surah_handler import GetDetailTafsirSurahHandler
from infra.fastapi.routers.surah_router import SurahRouter
from usecases.get_daftar_surah_ucase_impl import GetDaftarSurahUcaseImpl
from usecases.get_detail_ayat_surah_ucase_impl import GetDetailAyatSurahUcaseImpl
from usecases.get_detail_tafsir_surah_handler_impl import GetDetailTafsirSurahUcaseImpl

app = NewFastAPIApp(
    routers=[
        SurahRouter(
            get_daftar_surah_handler=GetDaftarSurahHandler(
                ucase=GetDaftarSurahUcaseImpl(),
            ),
            get_detail_ayat_surah_handler=GetDetailAyatSurahHandler(
                ucase=GetDetailAyatSurahUcaseImpl()
            ),
            get_detail_tafsir_surah_handler=GetDetailTafsirSurahHandler(
                ucase=GetDetailTafsirSurahUcaseImpl()
            )
        )
    ]
)
uvicorn.run(
    app,
    host='0.0.0.0',
    port=8000,
    log_level="info"
)
