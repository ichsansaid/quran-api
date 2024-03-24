from typing import Optional, List, Self

from pydantic import Field

from entity.ayat_entity import AyatEntity
from entity.surah_entity import SurahEntity, SurahBaseEntity
from entity.tafsir_entity import TafsirEntity


class SurahAggregate(SurahEntity):
    surat_selanjutnya: Optional[SurahBaseEntity] = Field(alias='suratSelanjutnya', default=None)
    surat_sebelumnya: Optional[SurahBaseEntity] = Field(alias='suratSebelumnya', default=None)
    ayat: Optional[List[AyatEntity]] = Field(default=None)
    tafsir: Optional[List[TafsirEntity]] = Field(default=None)

    @classmethod
    def from_entity[T: SurahEntity](cls, surah: T | List[T]) -> Self:
        if isinstance(surah, list):
            return [cls.model_validate(p, from_attributes=True) for p in surah]
        return cls.model_validate(surah, from_attributes=True)
