from typing import List

from pydantic import BaseModel, Field


class AyatEntity(BaseModel):
    nomor_ayat: int = Field(alias='nomorAyat')
    teks_arab: str = Field(alias='teksArab')
    teks_latin: str = Field(alias='teksLatin')
    audio: List[str] = Field(alias='audio')
    nomor_surah: int = Field(alias='nomorSurah')
