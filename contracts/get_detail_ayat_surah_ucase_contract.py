from abc import ABC, abstractmethod
from typing import Tuple

from dto.detail_ayat_surah_dto import DetailAyatSurahDto


class GetDetailAyatSurahUcaseContract(ABC):
    @abstractmethod
    def __call__(self, nomor_surah: int) -> Tuple[DetailAyatSurahDto, Exception]:
        pass
