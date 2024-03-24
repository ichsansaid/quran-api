from typing import Tuple

from contracts.alternate_quran_repo_contract import AlternateQuranRepoContract
from contracts.get_detail_tafsir_surah_ucase_contract import GetDetailTafsirSurahUcaseContract
from contracts.get_surah_by_no_ucase_contract import GetSurahByNoContract
from contracts.get_tafsir_by_no_contract import GetTafsirByNoSurahContract
from contracts.persistent_quran_repo_contract import PersistentQuranRepoContract
from dto.detail_tafsir_surah_dto import DetailTafsirSurahDto
from entity.surah_entity import SurahBaseEntity


class GetDetailTafsirSurahUcaseImpl(GetDetailTafsirSurahUcaseContract):
    def __init__(
            self,
            get_surah_by_no: GetSurahByNoContract,
            get_tafsir_by_no_surah: GetTafsirByNoSurahContract,
    ):
        self.get_tafsir_by_no_surah = get_tafsir_by_no_surah
        self.get_surah_by_no = get_surah_by_no

    def __call__(self, nomor_surah: int) -> Tuple[DetailTafsirSurahDto | None, Exception | None]:
        surah, err = self.get_surah_by_no(nomor_surah)
        result = DetailTafsirSurahDto.model_validate(surah, from_attributes=True)
        tafsir, err = self.get_tafsir_by_no_surah(surah.nomor)
        if err:
            return None, err
        result.tafsir = tafsir
        if nomor_surah < 114:
            surat_selanjutnya, err = self.get_surah_by_no(nomor_surah + 1)
            result.surat_selanjutnya = SurahBaseEntity.model_validate(surat_selanjutnya)
            if err:
                return None, err
        if nomor_surah > 1:
            surat_sebelumnya, err = self.get_surah_by_no(nomor_surah - 1)
            result.surat_sebelumnya = SurahBaseEntity.model_validate(surat_sebelumnya)
            if err:
                return None, err
        return result, None
