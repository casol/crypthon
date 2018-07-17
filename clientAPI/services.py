import requests
from crypthon.settings.base import get_env_variable


def get_specific_rate():
    """Get exchange rate between pair of requested assets at specific or current time."""
    url = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD'
    headers = {'X-CoinAPI-Key': API_KEY}
    exchange_rate = requests.get(url, headers=headers)
    return exchange_rate

def get_all_current_rates():
    """Get the current exchange rate between requested asset and all other assets."""
    url = 'https://rest.coinapi.io/v1/exchangerate/BTC'
    headers = {'X-CoinAPI-Key': API_KEY}
    exchange_rate_all = requests.get(url, headers=headers)
    return exchange_rate_all


# like this ?
class Client(object):
    """API Clinet for the CoinAPI.

    Entry point for making request to the CoinAPI. Provides methods to receive
    data for common API endpoints.

    """
    #API_KEY = get_env_variable('COINAPI_KEY')
    #API_BASE_URI = 'https://rest.coinapi.io/'

    def __init__(self, api_key):
        if not api_key:
            raise ValueError('Missing api key')
