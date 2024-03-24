from abc import ABC

from contracts.quran_repository_contract import QuranRepositoryContract


class AlternateQuranRepoContract(QuranRepositoryContract, ABC):
    pass
