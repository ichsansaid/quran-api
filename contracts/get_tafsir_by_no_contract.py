from abc import ABC, abstractmethod
from typing import Tuple, List

from entity.tafsir_entity import TafsirEntity


class GetTafsirByNoSurahContract(ABC):
    @abstractmethod
    def __call__(self, nomor_surah: int) -> Tuple[List[TafsirEntity] | None, Exception | None]:
        pass
