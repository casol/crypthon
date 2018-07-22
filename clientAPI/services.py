import requests
from urllib.parse import urljoin
from urllib.parse import quote

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

    def build_api_url(self, *args):
        """Build finale URL endpoint.

        Quote replace special characters in string using the %xx escape and
        the map function applies to a given function to each item of an iterable
        and returns a list of the results.
        """
        return urljoin(self.API_BASE_URI, '/'.join(map(quote, args)))

    def _get(self, *args):
        # https://rest.coinapi.io/v1/exchangerate/BTC/USD
        print(args)
        url = self.build_api_url(*args)
        response = requests.get(url, headers=self.headers)
        return response

    def get_specific_rate(self, **kwargs):
        """Get exchange rate between pair of requested assets at specific or current time.
        https://rest.coinapi.io/v1/exchangerate/BTC/USD'
        """
        currency_pair = kwargs.get('currency_pair', 'BTC/USD')
        exchange_rate = self._get('v1', 'exchangerate', currency_pair)
        return exchange_rate

    #def get_all_current_rates(self, **kwargs):
        #"""Get the current exchange rate between requested asset and all other assets."""
        #currency = kwargs.get('currency', 'BTC')
        #url = self.API_BASE_URI + 'v1/exchangerate/' + currency
        #exchange_rate_all = requests.get(url, headers=self.headers)
        #return exchange_rate_all
