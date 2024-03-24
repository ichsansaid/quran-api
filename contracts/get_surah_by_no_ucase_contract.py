from abc import ABC, abstractmethod
from typing import Tuple

from entity.surah_entity import SurahEntity


class GetSurahByNoContract(ABC):
    @abstractmethod
    def __call__(self, nomor_surah: int) -> Tuple[SurahEntity | None, Exception | None]:
        pass
