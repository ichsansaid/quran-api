from abc import ABC, abstractmethod
from typing import List, Tuple

from entity.surah_entity import SurahEntity


class GetDaftarSurahUcaseContract(ABC):
    @abstractmethod
    def __call__(self) -> Tuple[List[SurahEntity], Exception]:
        pass
