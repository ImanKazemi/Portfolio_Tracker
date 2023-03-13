# views.py - Django views file

from django.http import JsonResponse
from django.views import View
from django.conf import settings

from domain.repositories.coin_repository import MongoCoinRepository
from domain.services.coin_fetcher import CoinFetcher

# Get the MongoDB database settings from the Django settings
MONGODB_URI = f"{settings.DATABASES['default']['HOST']}:{settings.DATABASES['default']['PORT']}"
MONGODB_NAME = settings.DATABASES['default']['NAME']


class DataView(View):
    def get(self, request, *args, **kwargs):
        # collection = kwargs.get('collection')  # get collection name from URL
        repo = MongoCoinRepository(MONGODB_URI, MONGODB_NAME)
        data = repo.list()
        # data_dict = [{'id': d.id, 'name': d.name, 'symbol': d.symbol} for d in data]
        # return JsonResponse({'data': data_dict})
        return JsonResponse({'data': data})
