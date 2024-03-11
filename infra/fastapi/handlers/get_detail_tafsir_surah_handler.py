from contracts.get_detail_tafsir_surah_ucase_contract import GetDetailTafsirSurahUcaseContract
from dto.detail_tafsir_surah_dto import DetailTafsirSurahDto
from dto.response_dto import ResponseDto


class GetDetailTafsirSurahHandler:
    def __init__(self, ucase: GetDetailTafsirSurahUcaseContract = None):
        self.ucase = ucase

    def __call__(self, nomor_surah: int) -> ResponseDto[DetailTafsirSurahDto]:
        pass
