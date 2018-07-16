import requests
from crypthon.settings.base import get_env_variable

API_KEY = get_env_variable('COINAPI_KEY')


def get_specific_rate():
    """Get exchange rate between pair of requested assets at specific or current time."""
    url = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD'
    headers = {'X-CoinAPI-Key': API_KEY}
    exchange_rate = requests.get(url, headers=headers)
    return exchange_rate

def get_all_current_rates():
    """Get the current exchange rate between requested asset and all other assets."""
    url = 'https://rest.coinapi.io/v1/exchangerate/BTC'
    headers = {'X-CoinAPI-Key': '73034021-0EBC-493D-8A00-E0F138111F41'}
    exchange_rate_all = requests.get(url, headers=headers)
    return exchange_rate_all