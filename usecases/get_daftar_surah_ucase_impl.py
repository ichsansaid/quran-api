from typing import List

from contracts.get_daftar_surah_ucase_contract import GetDaftarSurahUcaseContract
from entity.surah_entity import SurahEntity


class GetDaftarSurahUcaseImpl(GetDaftarSurahUcaseContract):
    def __call__(self) -> List[SurahEntity]:
        # TODO: Silahkan bikin logic nya disini
        pass

