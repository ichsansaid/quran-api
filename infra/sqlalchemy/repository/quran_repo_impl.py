import json
from typing import List, Tuple

from sqlalchemy import select, insert
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from contracts.persistent_quran_repo_contract import PersistentQuranRepoContract
from entity.ayat_entity import AyatEntity
from entity.surah_entity import SurahEntity
from entity.tafsir_entity import TafsirEntity
from infra.sqlalchemy.engine.quran_engine import QuranEngine
from infra.sqlalchemy.schema.ayat_schema import AyatSchema
from infra.sqlalchemy.schema.surah_schema import SurahSchema
from infra.sqlalchemy.schema.tafsir_schema import TafsirSchema


class QuranRepoImpl(PersistentQuranRepoContract):

    def __init__(self, engine: QuranEngine):
        self.engine = engine

    def get_all_surah(self) -> Tuple[List[SurahEntity] | None, Exception | None]:
        conn = Session(self.engine)
        stmt = select(SurahSchema)
        try:
            data = conn.execute(stmt).all()
            return [SurahEntity.model_validate(p[0], from_attributes=True) for p in data], None
        except Exception as ex:
            return None, ex

    def get_surah_by_no(self, no: int) -> Tuple[SurahEntity | None, Exception | None]:
        conn = Session(self.engine)
        stmt = select(SurahSchema).where(SurahSchema.nomor == no)
        try:
            data = conn.execute(stmt).one()[0]
            return SurahEntity.model_validate(data, from_attributes=True), None
        except NoResultFound as ex:
            return None, None
        except Exception as ex:
            return None, ex

    def get_ayat_by_no(self, no: int) -> Tuple[List[AyatEntity] | None, Exception | None]:
        conn = Session(self.engine)
        stmt = select(AyatSchema).where(AyatSchema.nomor_surah == no)
        try:
            data = conn.execute(stmt).all()
            return [AyatEntity.model_validate(p[0], from_attributes=True) for p in data], None
        except Exception as ex:
            return None, ex

    def get_tafsir_by_no(self, no: int) -> Tuple[List[TafsirEntity] | None, Exception | None]:
        conn = Session(self.engine)
        stmt = select(TafsirSchema).where(TafsirSchema.surah == no)
        try:
            data = conn.execute(stmt).all()
            return [TafsirEntity.model_validate(p[0], from_attributes=True) for p in data], None
        except Exception as ex:
            return None, ex

    def save_all_surah(self, surah: List[SurahEntity]) -> Exception | None:
        conn = Session(self.engine)
        try:
            conn.execute(
                insert(SurahSchema),
                [
                    json.loads(p.model_dump_json()) for p in surah
                ]
            )
            conn.commit()
        except Exception as ex:
            return ex

    def save_surah(self, surah: SurahEntity) -> Exception:
        conn = Session(self.engine)
        try:
            conn.execute(
                insert(SurahSchema).values(**json.loads(surah.model_dump_json())),
            )
            conn.commit()
        except Exception as ex:
            return ex

    def save_ayat(self, ayat: AyatEntity) -> Exception:
        conn = Session(self.engine)
        try:
            conn.execute(
                insert(AyatSchema).values(**json.loads(ayat.model_dump_json())),
            )
            conn.commit()
        except Exception as ex:
            return ex

    def save_tafsir(self, tafsir: TafsirEntity) -> Exception:
        conn = Session(self.engine)
        try:
            conn.execute(
                insert(TafsirSchema).values(**json.loads(tafsir.model_dump_json())),
            )
            conn.commit()
        except Exception as ex:
            return ex

    def save_all_ayat(self, ayat: List[AyatEntity]) -> Exception:
        conn = Session(self.engine)
        try:
            conn.execute(
                insert(AyatSchema),
                [
                    json.loads(p.model_dump_json()) for p in ayat
                ]
            )
            conn.commit()
        except Exception as ex:
            return ex

    def save_all_tafsir(self, tafsir: List[TafsirEntity]) -> Exception:
        conn = Session(self.engine)
        try:
            conn.execute(
                insert(TafsirSchema),
                [
                    json.loads(p.model_dump_json()) for p in tafsir
                ]
            )
            conn.commit()
        except Exception as ex:
            return ex

