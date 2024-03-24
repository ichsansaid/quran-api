from sqlalchemy import String, JSON, Integer
from sqlalchemy.orm import mapped_column, Mapped

from infra.sqlalchemy.schema.base import Base


class AyatSchema(Base):
    __tablename__ = "tb_ayat"
    id: Mapped[int] = mapped_column(Integer(), autoincrement=True, primary_key=True)

    nomor_ayat: Mapped[int] = mapped_column(Integer(), name='nomor_ayat')
    nomor_surah: Mapped[int] = mapped_column(Integer(), name='nomor_surah')
    teks_arab: Mapped[str] = mapped_column(String(512), name="teks_arab")
    teks_latin: Mapped[str] = mapped_column(String(512), name="teks_latin")
    audio: Mapped[JSON] = mapped_column(JSON(), name='audio')
