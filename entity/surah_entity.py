from typing import List

from pydantic import BaseModel, Field


class SurahBaseEntity(BaseModel):
    nomor: int = Field(alias='nomor')
    nama: str = Field(alias='nama')
    nama_latin: str = Field(alias='namaLatin')
    jumlah_ayat: int = Field(alias='jumlahAyat')


class SurahEntity(SurahBaseEntity):
    tempat_turun: str = Field(alias='tempatTurun')
    arti: str = Field(alias='arti')
    deskripsi: str = Field(alias='deskripsi')
    audio_full: List[str] = Field(alias='audioFull')
