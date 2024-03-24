import json
from typing import List, Tuple

import urllib3

from contracts.alternate_quran_repo_contract import AlternateQuranRepoContract
from entity.ayat_entity import AyatEntity
from entity.surah_entity import SurahEntity
from entity.tafsir_entity import TafsirEntity


class EQuranAlternativeQuranRepo(AlternateQuranRepoContract):

    def __init__(self, url: str):
        self.http = urllib3.PoolManager()
        self.url = url

    def get_all_surah(self) -> Tuple[List[SurahEntity] | None, Exception | None]:
        response = self.http.request('get', url=f"{self.url}surat")
        if response.status == 500:
            return None, Exception("EQuran API Alternative quran repository is down")
        response_data = json.loads(response.data.decode('utf-8'))
        data = response_data['data']
        result = []
        for _data in data:
            surah = SurahEntity.model_validate(_data, from_attributes=False)
            result.append(surah)
        return result, None

    def get_surah_by_no(self, no: int) -> Tuple[SurahEntity | None, Exception | None]:
        response = self.http.request('get', url=f"{self.url}surat/{no}")
        if response.status == 500:
            return None, Exception("EQuran API Alternative quran repository is down")
        response_data = json.loads(response.data.decode('utf-8'))
        data = response_data['data']
        return SurahEntity.model_validate(data, from_attributes=False), None

    def get_ayat_by_no(self, no: int) -> Tuple[List[AyatEntity] | None, Exception | None]:
        response = self.http.request('get', url=f"{self.url}surat/{no}")
        if response.status == 500:
            return None, Exception("EQuran API Alternative quran repository is down")
        response_data = json.loads(response.data.decode('utf-8'))
        data = response_data['data']['ayat']
        result = []
        for _data in data:
            _data['nomorSurah'] = no
            ayat = AyatEntity.model_validate(_data,  from_attributes=False)
            result.append(ayat)
        return result, None

    def get_tafsir_by_no(self, no: int) -> Tuple[List[TafsirEntity] | None, Exception | None]:
        response = self.http.request('get', url=f"{self.url}tafsir/{no}")
        if response.status == 500:
            return None, Exception("EQuran API Alternative quran repository is down")
        response_data = json.loads(response.data.decode('utf-8'))
        data = response_data['data']['tafsir']
        result = []
        for _data in data:
            _data['surah'] = no
            tafsir = TafsirEntity.model_validate(_data, from_attributes=False)
            result.append(tafsir)
        return result, None

    def save_all_surah(self, surah: List[SurahEntity]) -> Exception:
        raise NotImplementedError("EQuran doesnt have this operation")

    def save_surah(self, surah: SurahEntity) -> Exception:
        raise NotImplementedError("EQuran doesnt have this operation")

    def save_ayat(self, ayat: AyatEntity) -> Exception:
        raise NotImplementedError("EQuran doesnt have this operation")

    def save_tafsir(self, tafsir: TafsirEntity) -> Exception:
        raise NotImplementedError("EQuran doesnt have this operation")

    def save_all_ayat(self, ayat: List[AyatEntity]) -> Exception:
        raise NotImplementedError("EQuran doesnt have this operation")

    def save_all_tafsir(self, tafsir: List[TafsirEntity]) -> Exception:
        raise NotImplementedError("EQuran doesnt have this operation")
