from abc import ABC, abstractmethod

from dto.detail_tafsir_surah_dto import DetailTafsirSurahDto


class GetDetailTafsirSurahAltRepoContract(ABC):
    @abstractmethod
    def __call__(self, nomor_surah: int) -> DetailTafsirSurahDto:
        pass
