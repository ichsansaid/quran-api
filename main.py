import os

import uvicorn
from sqlalchemy import create_engine, Engine

from infra.fastapi.app import NewFastAPIApp
from infra.fastapi.handlers.cdn_cache_aside_handler import CdnCacheAsideHandler
from infra.fastapi.handlers.get_daftar_surah_handler import GetDaftarSurahHandler
from infra.fastapi.handlers.get_detail_ayat_surah_handler import GetDetailAyatSurahHandler
from infra.fastapi.handlers.get_detail_tafsir_surah_handler import GetDetailTafsirSurahHandler
from infra.fastapi.routers.surah_router import SurahRouter
from infra.http.repository.equran_alternative_quran_repo import EQuranAlternativeQuranRepo
from infra.sqlalchemy.engine.quran_engine import QuranEngine
from infra.sqlalchemy.repository.quran_repo_impl import QuranRepoImpl
from infra.sqlalchemy.schema.ayat_schema import AyatSchema
from infra.sqlalchemy.schema.surah_schema import SurahSchema
from infra.sqlalchemy.schema.tafsir_schema import TafsirSchema
from usecases.get_ayat_by_no_surah_ucase_impl import GetAyatByNoSurahUcaseImpl
from usecases.get_daftar_surah_ucase_impl import GetDaftarSurahUcaseImpl
from usecases.get_detail_ayat_surah_ucase_impl import GetDetailAyatSurahUcaseImpl
from usecases.get_detail_tafsir_surah_ucase_impl import GetDetailTafsirSurahUcaseImpl
from usecases.get_surah_by_no_ucase_impl import GetSurahByNoUcaseImpl
from usecases.get_tafsir_by_no_surah_ucase_impl import GetTafsirByNoSurahUcaseImpl

engine: QuranEngine | Engine = create_engine("sqlite:///store/sqlite/quran.db")

persistent_repo = QuranRepoImpl(
    engine=engine,
)
alt_repo = EQuranAlternativeQuranRepo(
    url="https://equran.id/api/v2/"
)
get_surah_by_no = GetSurahByNoUcaseImpl(
    persistent_repo=persistent_repo,
    alt_repo=alt_repo,
)
get_ayat_by_no = GetAyatByNoSurahUcaseImpl(
    persistent_repo=persistent_repo,
    alt_repo=alt_repo,
)
get_tafsir_by_no = GetTafsirByNoSurahUcaseImpl(
    persistent_repo=persistent_repo,
    alt_repo=alt_repo,
)

SurahSchema.metadata.create_all(engine)
AyatSchema.metadata.create_all(engine)
TafsirSchema.metadata.create_all(engine)

app = NewFastAPIApp(
    routers=[
        SurahRouter(
            get_daftar_surah_handler=GetDaftarSurahHandler(
                ucase=GetDaftarSurahUcaseImpl(
                    alt_repo=alt_repo,
                    persistent_repo=persistent_repo
                ),
            ),
            get_detail_ayat_surah_handler=GetDetailAyatSurahHandler(
                ucase=GetDetailAyatSurahUcaseImpl(
                    get_surah_by_no=get_surah_by_no,
                    get_ayat_by_no_surah=get_ayat_by_no
                )
            ),
            get_detail_tafsir_surah_handler=GetDetailTafsirSurahHandler(
                ucase=GetDetailTafsirSurahUcaseImpl(
                    get_surah_by_no=get_surah_by_no,
                    get_tafsir_by_no_surah=get_tafsir_by_no
                )
            )
        )
    ]
)()

app.mount("/quran-static", CdnCacheAsideHandler(directory=os.path.join("store", "static", "quran"), fallback_caching_url="https://equran.nos.wjv-1.neo.id/audio-full/"),
          name="quran")

uvicorn.run(
    app,
    host='0.0.0.0',
    port=8000,
    log_level="info"
)
