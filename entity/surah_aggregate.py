from typing import Optional, Self, List

from pydantic import Field

from entity.ayat_entity import AyatEntity
from entity.surah_entity import SurahEntity, SurahBaseEntity
from entity.tafsir_entity import TafsirEntity


class SurahAggregate(SurahEntity):
    surat_selanjutnya: Optional[SurahBaseEntity] = Field(alias='suratSelanjutnya')
    surat_sebelumnya: Optional[SurahBaseEntity] = Field(alias='suratSebelumnya')
    ayat: List[AyatEntity] = Field()
    tafsir: List[TafsirEntity] = Field()

    @classmethod
    def from_entity[T: SurahEntity](cls, surah: T | List[T]) -> T | List[T]:
        if isinstance(surah, list):
            return [cls.model_validate(p) for p in surah]
        return cls.model_validate(surah)
