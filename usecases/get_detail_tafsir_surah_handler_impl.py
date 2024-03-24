from typing import Tuple

from contracts.alternate_quran_repo_contract import AlternateQuranRepoContract
from contracts.get_detail_tafsir_surah_ucase_contract import GetDetailTafsirSurahUcaseContract
from contracts.get_surah_by_no_ucase_contract import GetSurahByNoContract
from contracts.persistent_quran_repo_contract import PersistentQuranRepoContract
from dto.detail_tafsir_surah_dto import DetailTafsirSurahDto


class GetDetailTafsirSurahUcaseImpl(GetDetailTafsirSurahUcaseContract):
    def __init__(self, persistent_repo: PersistentQuranRepoContract, alt_repo: AlternateQuranRepoContract, get_surah_by_no: GetSurahByNoContract):
        self.get_surah_by_no = get_surah_by_no
        self.persistent_repo = persistent_repo
        self.alt_repo = alt_repo

    def __call__(self, nomor_surah: int) -> Tuple[DetailTafsirSurahDto | None, Exception | None]:
        surah, err = self.get_surah_by_no(nomor_surah)

        result = DetailTafsirSurahDto.model_validate(surah)
        tafsir, err = self.persistent_repo.get_tafsir_by_no(surah.nomor)
        if err:
            return None, err
        result.tafsir = tafsir
        if nomor_surah < 114:
            result.surat_selanjutnya, err = self.get_surah_by_no(nomor_surah + 1)
            if err:
                return None, err
        if nomor_surah > 1:
            result.surat_sebelumnya, err = self.get_surah_by_no(nomor_surah - 1)
            if err:
                return None, err
        return result, None
