from typing import List, Dict

from pydantic import BaseModel, Field, ConfigDict


class SurahBaseEntity(BaseModel):
    nomor: int = Field(alias='nomor')
    nama: str = Field(alias='nama')
    nama_latin: str = Field(alias='namaLatin')
    jumlah_ayat: int = Field(alias='jumlahAyat')

    model_config = ConfigDict(
        populate_by_name=True,
    )


class SurahEntity(SurahBaseEntity):
    tempat_turun: str = Field(alias='tempatTurun')
    arti: str = Field(alias='arti')
    deskripsi: str = Field(alias='deskripsi')
    audio_full: Dict[str, str] = Field(alias='audioFull')
