from abc import ABC, abstractmethod
from typing import Tuple, List

from entity.ayat_entity import AyatEntity
from entity.surah_entity import SurahEntity


class GetAyatByNoSurahContract(ABC):
    @abstractmethod
    def __call__(self, nomor_surah: int) -> Tuple[List[AyatEntity] | None, Exception | None]:
        pass
