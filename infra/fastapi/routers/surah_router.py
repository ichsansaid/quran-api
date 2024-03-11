from fastapi import APIRouter

from infra.fastapi.handlers.get_daftar_surah_handler import GetDaftarSurahHandler
from infra.fastapi.handlers.get_detail_ayat_surah_handler import GetDetailAyatSurahHandler
from infra.fastapi.handlers.get_detail_tafsir_surah_handler import GetDetailTafsirSurahHandler


class SurahRouter:

    def __init__(
            self,
            get_daftar_surah_handler: GetDaftarSurahHandler,
            get_detail_ayat_surah_handler: GetDetailAyatSurahHandler,
            get_detail_tafsir_surah_handler: GetDetailTafsirSurahHandler,
    ):
        self.get_detail_tafsir_surah_handler = get_detail_tafsir_surah_handler
        self.get_detail_ayat_surah_handler = get_detail_ayat_surah_handler
        self.get_daftar_surah_handler = get_daftar_surah_handler

    def __call__(self, *args, **kwargs) -> APIRouter:
        router = APIRouter(
            prefix="/surat"
        )
        router.get("")(self.get_daftar_surah_handler.__call__)
        router.get("{nomor_surah}/ayat")(self.get_detail_ayat_surah_handler.__call__)
        router.get("{nomor_surah}/tafsir")(self.get_detail_tafsir_surah_handler.__call__)
        return router
