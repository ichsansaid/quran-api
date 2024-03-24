from contracts.get_detail_ayat_surah_ucase_contract import GetDetailAyatSurahUcaseContract
from dto.detail_ayat_surah_dto import DetailAyatSurahDto
from dto.response_dto import ResponseDto


class GetDetailAyatSurahHandler:
    def __init__(self, ucase: GetDetailAyatSurahUcaseContract = None):
        self.ucase = ucase

    def __call__(self, nomor_surah: int) -> ResponseDto[DetailAyatSurahDto]:
        result, err = self.ucase(nomor_surah)
        if err:
            raise err
        return ResponseDto(
            code=200,
            message="Data retrieved successfully",
            data=result
        )
