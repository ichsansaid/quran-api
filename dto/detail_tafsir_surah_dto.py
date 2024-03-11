from typing import List, Optional

from pydantic import Field

from entity.surah_entity import SurahEntity, SurahBaseEntity
from entity.tafsir_entity import TafsirEntity


class DetailTafsirSurahDto(SurahEntity):
    tafsir: List[TafsirEntity]
    surat_selanjutnya: Optional[SurahBaseEntity] = Field(alias='suratSelanjutnya')
    surat_sebelumnya: Optional[SurahBaseEntity] = Field(alias='suratSebelumnya')
