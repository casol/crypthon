from __future__ import absolute_import, unicode_literals
from celery import shared_task

from .services import Client_CryptoCompare, Client
from .models import Crypto_Currency, Currency_Trending_Info, Fiat_Currency


@shared_task
def send_api_request():

    client_w = Client_CryptoCompare()
    xx = client_w.get_specific_rate_full_data(cryptocurrencies='BTC', currencies='USD').json()

    return  xx['DISPLAY']['BTC']['USD']['PRICE']



class JsonToDB(object):
    """Deserialize a json API response and saves to the database."""

    def __init__(self):
        self.client = Client_CryptoCompare()
        # Retrieving all field instances of a model
        self.get_model_fields(model=Currency_Trending_Info)

    def get_model_fields(self, model):
        """Returns a list of fields associated with a model"""
        model_fields = [field.name.replace('_', '').upper() for field in model._meta.get_fields()]
        return model_fields

    def adjust_to_the_model(self,*args, **kwargs):
        """Adjust API response to match model fields."""
        data_dic = {}
        for key, value in kwargs.items():
            if key in args:
                data_dic[key.lower()] = value

        return data_dic


    def save_to_database(self, *args, **kwargs):
        # save to the database
        #trending_info = kwargs.get()

        entry = Crypto_Currency(crypto_currency=args[0], price=kwargs.get('PRICE'),
                                unix_timestamp=kwargs.get('lastupdate'))
        entry.save()
        entry_fiat = Fiat_Currency(crypto_currency=entry,  currency=args[1])

        entry_info = Currency_Trending_Info(kwargs)


    def new_entry(self, crypto, fiat):

        response = self.client.get_specific_rate_full_data(cryptocurrencies=crypto,
                                                           currencies=fiat).json()
        response_dic = response['DISPLAY'][crypto][fiat]
        save = self.save_to_database(crypto, fiat, response_dic)

        return response_dic



# call
test = JsonToDB()
test.new_entry('BTC', 'USD',)