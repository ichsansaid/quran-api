from typing import List, Optional

from pydantic import Field

from entity.ayat_entity import AyatEntity
from entity.surah_entity import SurahEntity, SurahBaseEntity


class DetailAyatSurahDto(SurahEntity):
    ayat: List[AyatEntity]
    surat_selanjutnya: Optional[SurahBaseEntity] = Field(alias='suratSelanjutnya')
    surat_sebelumnya: Optional[SurahBaseEntity] = Field(alias='suratSebelumnya')
