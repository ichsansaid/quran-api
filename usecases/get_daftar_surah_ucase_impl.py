from typing import List, Tuple

from contracts.alternate_quran_repo_contract import AlternateQuranRepoContract
from contracts.get_daftar_surah_ucase_contract import GetDaftarSurahUcaseContract
from contracts.persistent_quran_repo_contract import PersistentQuranRepoContract
from entity.surah_entity import SurahEntity


class GetDaftarSurahUcaseImpl(GetDaftarSurahUcaseContract):
    def __init__(self, persistent_repo: PersistentQuranRepoContract, alt_repo: AlternateQuranRepoContract):
        self.persistent_repo = persistent_repo
        self.alt_repo = alt_repo

    def __call__(self) -> Tuple[List[SurahEntity] | None, Exception | None]:
        data, err = self.persistent_repo.get_all_surah()
        if err:
            return None, err
        if len(data) == 0:
            newest_data, err = self.alt_repo.get_all_surah()
            if err:
                return None, err
            err = self.persistent_repo.save_all_surah(newest_data)
            if err:
                return None, err
            return newest_data, None


