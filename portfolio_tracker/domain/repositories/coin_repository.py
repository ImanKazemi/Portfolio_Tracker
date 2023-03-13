from abc import ABC, abstractmethod
from typing import List

from pymongo import MongoClient

from domain.entities.coin import Coin


class CoinRepository(ABC):

    @abstractmethod
    def save(self, coin: Coin) -> None:
        pass

    @abstractmethod
    def get(self, id: str) -> Coin:
        pass

    @abstractmethod
    def list(self) -> List[Coin]:
        pass


class MongoCoinRepository(CoinRepository):
    def __init__(self, db_uri: str, db_name: str):
        self.client = MongoClient(db_uri)
        self.db = self.client[db_name]
        self.collection = self.db['coins']

    def save(self, coin: Coin) -> None:
        data_dict = coin.__dict__
        self.collection.update_one({'_id': coin.id}, {'$set': data_dict}, upsert=True)

    def get(self, id: str):
        coin_dict = self.collection.find_one({'_id': id})
        if coin_dict:
            coin_dict.pop('_id')
            return Coin(**coin_dict)
        else:
            return None
        
    def list(self) -> List[Coin]:
        coin_list = []
        for coin_list in self.collection.find():
            coin_list.pop('_id')
            coin_list.append(Coin(**coin_list))
        return coin_list
