from abc import ABC, abstractmethod
from typing import List

from entity.surah_entity import SurahEntity


class GetDaftarSurahRepoContract(ABC):
    @abstractmethod
    def __call__(self) -> List[SurahEntity]:
        pass
