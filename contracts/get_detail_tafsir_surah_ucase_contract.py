from abc import ABC, abstractmethod
from typing import Tuple

from dto.detail_tafsir_surah_dto import DetailTafsirSurahDto


class GetDetailTafsirSurahUcaseContract(ABC):
    @abstractmethod
    def __call__(self, nomor_surah: int) -> Tuple[DetailTafsirSurahDto | None, Exception | None]:
        pass
