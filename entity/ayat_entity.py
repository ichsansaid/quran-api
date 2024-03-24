from typing import List, Dict

from pydantic import BaseModel, Field, ConfigDict


class AyatEntity(BaseModel):
    nomor_ayat: int = Field(alias='nomorAyat')
    teks_arab: str = Field(alias='teksArab')
    teks_latin: str = Field(alias='teksLatin')
    audio: Dict[str, str] = Field(alias='audio')
    nomor_surah: int = Field(alias='nomorSurah')

    model_config = ConfigDict(
        populate_by_name=True,
    )
