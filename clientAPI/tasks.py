from __future__ import absolute_import, unicode_literals
from celery import shared_task

from .services import ClientCryptoCompare, Client
from .services import ResponseDeserializer

@shared_task
def send_api_request_usd():
    """Get the latest data from an API."""
    callsave = ResponseDeserializer()
    callsave.new_entry('BTC', 'USD')
    callsave.new_entry('ETH', 'USD')
    callsave.new_entry('LTC', 'USD')
    callsave.new_entry('XRP', 'USD')



@shared_task
def send_api_request_eur():
    """Get the latest data from an API."""
    callsave = ResponseDeserializer()
    callsave.new_entry('BTC', 'EUR')
    callsave.new_entry('ETH', 'EUR')
    callsave.new_entry('LTC', 'EUR')
    callsave.new_entry('XRP', 'EUR')


