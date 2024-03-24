from sqlalchemy import String, JSON, Integer
from sqlalchemy.orm import mapped_column, Mapped

from infra.sqlalchemy.schema.base import Base


class SurahSchema(Base):
    __tablename__ = "tb_surah"

    nomor: Mapped[int] = mapped_column(primary_key=True, name='nomor')
    nama: Mapped[str] = mapped_column(String(124), name='nama')
    nama_latin: Mapped[str] = mapped_column(Integer(), name='nama_latin')
    jumlah_ayat: Mapped[int] = mapped_column(Integer(), name='jumlah_ayat')

    tempat_turun: Mapped[str] = mapped_column(String(124), name='tempat_turun')
    arti: Mapped[str] = mapped_column(String(124), name='arti')
    deskripsi: Mapped[str] = mapped_column(String(124), name='deskripsi')
    audio_full: Mapped[JSON] = mapped_column(JSON(), name='audio_full')