from typing import Tuple, List

from contracts.alternate_quran_repo_contract import AlternateQuranRepoContract
from contracts.get_tafsir_by_no_contract import GetTafsirByNoSurahContract
from contracts.persistent_quran_repo_contract import PersistentQuranRepoContract
from entity.tafsir_entity import TafsirEntity


class GetTafsirByNoSurahUcaseImpl(GetTafsirByNoSurahContract):
    def __init__(self, persistent_repo: PersistentQuranRepoContract, alt_repo: AlternateQuranRepoContract):
        self.persistent_repo = persistent_repo
        self.alt_repo = alt_repo

    def __call__(self, nomor_surah: int) -> Tuple[List[TafsirEntity] | None, Exception | None]:
        tafsir, err = self.persistent_repo.get_tafsir_by_no(nomor_surah)
        if err:
            return None, err
        if len(tafsir) == 0:
            tafsir, err = self.alt_repo.get_tafsir_by_no(nomor_surah)
            if err:
                return None, err
            err = self.persistent_repo.save_all_tafsir(tafsir)
            if err:
                return None, err
        return tafsir, None
