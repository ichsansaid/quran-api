from abc import ABC, abstractmethod
from typing import Tuple, List

from entity.ayat_entity import AyatEntity
from entity.surah_aggregate import SurahAggregate
from entity.surah_entity import SurahEntity
from entity.tafsir_entity import TafsirEntity


class QuranRepositoryContract(ABC):
    @abstractmethod
    def get_all_surah(self) -> Tuple[List[SurahEntity], Exception]:
        pass

    @abstractmethod
    def get_surah_by_no(self, no: int) -> Tuple[SurahEntity | None, Exception]:
        pass

    @abstractmethod
    def get_ayat_by_no(self, no: int) -> Tuple[List[AyatEntity], Exception]:
        pass

    @abstractmethod
    def get_tafsir_by_no(self, no: int) -> Tuple[List[TafsirEntity], Exception]:
        pass

    @abstractmethod
    def save_all_surah(self, surah: List[SurahEntity]) -> Exception:
        pass

    @abstractmethod
    def save_all_ayat(self, ayat: List[AyatEntity]) -> Exception:
        pass

    @abstractmethod
    def save_all_tafsir(self, tafsir: List[TafsirEntity]) -> Exception:
        pass

    @abstractmethod
    def save_surah(self, surah: SurahEntity) -> Exception:
        pass

    @abstractmethod
    def save_ayat(self, ayat: AyatEntity) -> Exception:
        pass

    @abstractmethod
    def save_tafsir(self, tafsir: TafsirEntity) -> Exception:
        pass
