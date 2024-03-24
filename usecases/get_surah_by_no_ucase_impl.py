from typing import Tuple

from contracts.alternate_quran_repo_contract import AlternateQuranRepoContract
from contracts.get_surah_by_no_ucase_contract import GetSurahByNoContract
from contracts.persistent_quran_repo_contract import PersistentQuranRepoContract
from entity.surah_entity import SurahEntity


class GetSurahByNoUcaseImpl(GetSurahByNoContract):
    def __init__(self, persistent_repo: PersistentQuranRepoContract, alt_repo: AlternateQuranRepoContract):
        self.persistent_repo = persistent_repo
        self.alt_repo = alt_repo

    def __call__(self, nomor_surah: int) -> Tuple[SurahEntity | None, Exception | None]:
        surah, err = self.persistent_repo.get_surah_by_no(nomor_surah)
        if err:
            return None, err
        if surah is None:
            surah, err = self.alt_repo.get_surah_by_no(nomor_surah)
            if err:
                return None, err
            err = self.persistent_repo.save_surah(surah)
            if err:
                return None, err
        return surah, None
