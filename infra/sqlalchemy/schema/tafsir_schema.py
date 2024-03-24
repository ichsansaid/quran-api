from sqlalchemy import String, Integer
from sqlalchemy.orm import mapped_column, Mapped

from infra.sqlalchemy.schema.base import Base


class TafsirSchema(Base):
    __tablename__ = "tb_tafsir"
    id: Mapped[int] = mapped_column(Integer(), autoincrement=True, primary_key=True)

    surah: Mapped[int] = mapped_column(Integer(), name='surah')
    ayat: Mapped[int] = mapped_column(Integer(), name='ayat')
    teks: Mapped[str] = mapped_column(String(512), name='teks')