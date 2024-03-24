from typing import Tuple

from contracts.get_ayat_by_no_contract import GetAyatByNoSurahContract
from contracts.get_detail_ayat_surah_ucase_contract import GetDetailAyatSurahUcaseContract
from contracts.get_surah_by_no_ucase_contract import GetSurahByNoContract
from dto.detail_ayat_surah_dto import DetailAyatSurahDto
from entity.surah_entity import SurahBaseEntity


class GetDetailAyatSurahUcaseImpl(GetDetailAyatSurahUcaseContract):
    def __init__(
            self,
            get_surah_by_no: GetSurahByNoContract,
            get_ayat_by_no_surah: GetAyatByNoSurahContract,
    ):
        self.get_surah_by_no = get_surah_by_no
        self.get_ayat_by_no_surah = get_ayat_by_no_surah

    def __call__(self, nomor_surah: int) -> Tuple[DetailAyatSurahDto | None, Exception | None]:
        surah, err = self.get_surah_by_no(nomor_surah)
        if err:
            return None, err
        result = DetailAyatSurahDto.from_entity(surah)

        ayat, err = self.get_ayat_by_no_surah(surah.nomor)
        if err:
            return None, err
        result.ayat = ayat

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
