from abc import ABC, abstractmethod
from typing import Tuple, List

from entity.ayat_entity import AyatEntity
from entity.surah_aggregate import SurahAggregate
from entity.surah_entity import SurahEntity


class QuranRepositoryContract(ABC):
    @abstractmethod
    def get_all_surah(self) -> Tuple[List[SurahEntity], Exception]:
        pass

    @abstractmethod
    def get_surah_by_no(self, no: int) -> Tuple[SurahEntity, Exception]:
        pass

    @abstractmethod
    def get_ayat_by_no(self, no: int) -> Tuple[List[AyatEntity], Exception]:
        pass

    @abstractmethod
    def get_tafsir_by_no(self, no: int) -> Tuple[List[AyatEntity], Exception]:
        pass
