
from domain.entities.coin import Coin
from domain.repositories import coin_repository


class CoinFetcher:
    def __init__(self, repo: coin_repository):
        self.repo = repo

    def fetch_data(self):
        coins = self.repo.find_all()
        coin = Coin(id='1', name='2', symbol='3')
        self.repo.save(coin.to_dict())
        
        # if not coins:
        #     api_data = self.fetch_from_api()
        #     for d in api_data:
        #         coin = coin(id=d['id'], name=d['name'], symbol=d['symbol'])
        #         self.repo.save(coin)
        #     data = self.repo.find_all()
        # return data
        return ""

    def fetch_from_api(self):
        # code to fetch data from external APIs
        pass
