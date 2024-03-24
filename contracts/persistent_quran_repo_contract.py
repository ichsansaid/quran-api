from abc import ABC

from contracts.quran_repository_contract import QuranRepositoryContract


class PersistentQuranRepoContract(QuranRepositoryContract, ABC):
    pass
