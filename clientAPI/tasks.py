from __future__ import absolute_import, unicode_literals
from celery import shared_task

from .services import Client_CryptoCompare, Client
from .models import Crypto_Currency, Currency_Trending_Info, Fiat_Currency


@shared_task
def send_api_request():

    client_w = Client_CryptoCompare()
    xx = client_w.get_specific_rate_full_data(cryptocurrencies='BTC', currencies='USD').json()

    return  xx['RAW']['BTC']['USD']['PRICE']



class JsonToDB(object):
    """Deserialize a json API response and save to the database."""

    def __init__(self):
        self.client = Client_CryptoCompare()
        # Retrieving all field instances of a model
        self.model_fields= self._get_model_fields(model=Currency_Trending_Info)

    def _get_model_fields(self, model):
        """Returns a list of fields associated with a model"""
        return [field.name.upper() for field in model._meta.get_fields()]

    def adjust_to_the_model(self,*args, **kwargs):
        """Adjust API response to match model fields."""

        data_dic = {}
        for key, value in kwargs.items():
            if key in args:
                # rounding numbers
                try:
                    #value = float(value)
                    value = round(value, 4)
                except TypeError:
                    pass
                data_dic[key.lower()] = value

        return data_dic


    def save_to_database(self, *args, **kwargs):
        # save to the database
        entry = Crypto_Currency(crypto_currency=args[0],
                                price=kwargs.get('PRICE'),
                                unix_timestamp=11111111)
        entry.save()
        fiat_entry = Fiat_Currency(crypto_currency=entry, currency=args[1])
        fiat_entry.save()
        currency_info = Currency_Trending_Info(crypto_currency=entry, **kwargs)
        currency_info.save()


    def new_entry(self, crypto, fiat):

        response = self.client.get_specific_rate_full_data(cryptocurrencies=crypto,
                                                           currencies=fiat).json()
        response_dic = response['RAW'][crypto][fiat]
        data_dic = self.adjust_to_the_model(*self.model_fields, **response_dic)
        self.save_to_database(crypto, fiat, **data_dic)


# brakuje _ podkreslenia ..., argument cena i czas tez

# call
#test = JsonToDB()
#test.new_entry('BTC', 'USD',)