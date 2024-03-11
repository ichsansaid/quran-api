from pydantic import BaseModel, Field


class TafsirEntity(BaseModel):
    ayat: int = Field(alias='ayat')
    teks: str
