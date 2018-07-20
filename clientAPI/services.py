import requests


class Client(object):
    """API Clinet for the CoinAPI.

    Entry point for making request to the CoinAPI. Provides methods to receive
    data for common API endpoints.

    """

    API_BASE_URI = 'https://rest.coinapi.io/'

    def __init__(self, api_key,):
        if not api_key:
            raise ValueError('Missing api key')

        self.API_KEY = api_key
        self.headers = {'X-CoinAPI-Key': self.API_KEY}


    def _get(self, *args, **kwargs):
        # https://rest.coinapi.io/v1/exchangerate/BTC/USD
        # API_BASE_URI      +     v1   + exchangerate + dict
        uri = self.API_BASE_URI
        url = uri + args[0] + args[1]
        asset = kwargs.get('data', None)
        url = 'www.ddd'
        response = requests.get(url, headers=self.headers)
        return response

        # self._get('v1', 'exchangerate', currency_pair)

    def get_specific_rate(self, **kwargs):
        """Get exchange rate between pair of requested assets at specific or current time.
        https://rest.coinapi.io/v1/exchangerate/BTC/USD'
        """
        # dictionary.get('Key', default_value') e.g. btc/usd or ltc/euro
        currency_pair = kwargs.get('currency_pair', 'BTC/USD')
        url = self.API_BASE_URI + 'v1/exchangerate/' + currency_pair
        # self._get('v1', 'exchangerate', currency_pair)
        exchange_rate = requests.get(url, headers=self.headers)
        return exchange_rate

    def get_all_current_rates(self, **kwargs):
        """Get the current exchange rate between requested asset and all other assets."""
        currency = kwargs.get('currency', 'BTC')
        url = self.API_BASE_URI + 'v1/exchangerate/' + currency
        exchange_rate_all = requests.get(url, headers=self.headers)
        return exchange_rate_all
