from abc import ABC, abstractmethod

from dto.detail_ayat_surah_dto import DetailAyatSurahDto


class GetDetailAyatSurahUcaseContract(ABC):
    @abstractmethod
    def __call__(self, nomor_surah: int) -> DetailAyatSurahDto:
        pass