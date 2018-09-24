from __future__ import absolute_import, unicode_literals
from celery import shared_task

from .services import Client_CryptoCompare, Client


@shared_task
def send_api_request():

    client_w = Client_CryptoCompare()
    xx = client_w.get_specific_rate_full_data(cryptocurrencies='BTC', currencies='USD').json()

    return  xx['DISPLAY']['BTC']['USD']['PRICE']