from typing import Tuple, List

from contracts.alternate_quran_repo_contract import AlternateQuranRepoContract
from contracts.get_ayat_by_no_contract import GetAyatByNoSurahContract
from contracts.persistent_quran_repo_contract import PersistentQuranRepoContract
from entity.ayat_entity import AyatEntity


class GetAyatByNoSurahUcaseImpl(GetAyatByNoSurahContract):
    def __init__(self, persistent_repo: PersistentQuranRepoContract, alt_repo: AlternateQuranRepoContract):
        self.persistent_repo = persistent_repo
        self.alt_repo = alt_repo

    def __call__(self, nomor_surah: int) -> Tuple[List[AyatEntity] | None, Exception | None]:
        ayat, err = self.persistent_repo.get_ayat_by_no(nomor_surah)
        if err:
            return None, err
        if len(ayat) == 0:
            ayat, err = self.alt_repo.get_ayat_by_no(nomor_surah)
            if err:
                return None, err
            err = self.persistent_repo.save_all_ayat(ayat)
            if err:
                return None, err
        return ayat, None
