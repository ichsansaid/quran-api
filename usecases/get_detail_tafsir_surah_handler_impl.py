from contracts.get_detail_tafsir_surah_ucase_contract import GetDetailTafsirSurahUcaseContract
from dto.detail_tafsir_surah_dto import DetailTafsirSurahDto


class GetDetailTafsirSurahUcaseImpl(GetDetailTafsirSurahUcaseContract):
    def __call__(self, nomor_surah: int) -> DetailTafsirSurahDto:
        # TODO: Silahkan bikin logic nya disini
        pass