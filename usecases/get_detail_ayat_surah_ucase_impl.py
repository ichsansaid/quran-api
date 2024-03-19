from contracts.get_detail_ayat_surah_ucase_contract import GetDetailAyatSurahUcaseContract
from dto.detail_ayat_surah_dto import DetailAyatSurahDto


class GetDetailAyatSurahUcaseImpl(GetDetailAyatSurahUcaseContract):
    def __call__(self, nomor_surah: int) -> DetailAyatSurahDto:
        # TODO: Silahkan bikin logic nya disini
        pass