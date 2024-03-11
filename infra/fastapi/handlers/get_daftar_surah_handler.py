from typing import List

from contracts.get_daftar_surah_ucase_contract import GetDaftarSurahUcaseContract
from dto.response_dto import ResponseDto
from entity.surah_entity import SurahEntity


class GetDaftarSurahHandler:
    def __init__(self, ucase: GetDaftarSurahUcaseContract = None):
        self.ucase = ucase

    def __call__(self) -> ResponseDto[List[SurahEntity]]:
        pass
