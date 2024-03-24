from pydantic import BaseModel, Field


class TafsirEntity(BaseModel):
    surah: int = Field(alias='surah')
    ayat: int = Field(alias='ayat')
    teks: str
