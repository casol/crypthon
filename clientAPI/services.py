import requests
from urllib.parse import urljoin
from urllib.parse import quote

from .models import CryptoCurrency, CurrencyTrendingInfo, FiatCurrency


class Client(object):
    """API Client for the CoinAPI.

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
        """Build response object.

        Creates a HTTP request, uses the API key to authorized access.

        """
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

    def get_all_current_rates(self, **kwargs):
        """Get the current exchange rate between requested asset and all other assets."""
        currency = kwargs.get('currency', 'BTC')
        exchange_rate_all = self._get('v1', 'exchangerate', currency)
        return exchange_rate_all

    def list_all_periods(self, **kwargs):
        pass


class ClientCryptoCompare(object):
    """API Client for the CryptoCompare.

    Entry point for making request to the CryptoCompare. Provides methods to receive
    data for current trading info.

    """

    API_BASE_URI = 'https://min-api.cryptocompare.com/data/'

    def build_api_url(self, *args):
        """Build finale URL endpoint."""
        join_path = ''.join(args)
        return urljoin(self.API_BASE_URI, join_path)

    def _get(self, *args):
        """Build response object, creates a HTTP request."""
        url = self.build_api_url(*args)
        response = requests.get(url)
        return response


    def get_specific_rate_full_data(self, cryptocurrencies, currencies):
        """Returns a market's last price as well as other
        stats based on a 24-hour sliding window.

        """
        # Comma separated cryptocurrency symbols list
        exchange_rate = self._get('pricemultifull?fsyms=', cryptocurrencies,
                                  '&tsyms=', currencies)
        return exchange_rate


class ResponseDeserializer(object):
    """Deserialize a json API response and save to the database."""

    def __init__(self):
        self.client = ClientCryptoCompare()
        # Retrieving all field instances of a model
        self.model_fields= self._get_model_fields(model=CurrencyTrendingInfo)

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
                    value = round(value, 4)
                except TypeError:
                    pass
                data_dic[key.lower()] = value

        return data_dic


    def save_to_database(self, *args, **kwargs):
        """Create an object and save to the database."""
        entry = CryptoCurrency(crypto_currency=args[0],
                               price=args[2],
                               unix_timestamp=args[3])
        entry.save()
        fiat_entry = FiatCurrency(crypto_currency=entry, currency=args[1])
        fiat_entry.save()
        currency_info = CurrencyTrendingInfo(crypto_currency=entry, **kwargs)
        currency_info.save()


    def new_entry(self, crypto, fiat):
        """Call an API and save to the database a new entry.

        Function takes two arguments:
        crypto -- the cryptocurrency e.g. BTC
        fiat -- the fiat currency e.g. USD
        """
        response = self.client.get_specific_rate_full_data(cryptocurrencies=crypto,
                                                           currencies=fiat).json()
        response_dic = response['RAW'][crypto][fiat]
        price = response_dic.get('PRICE')
        unix_timestamp = response_dic.get('LASTUPDATE')
        data_dic = self.adjust_to_the_model(*self.model_fields, **response_dic)
        self.save_to_database(crypto, fiat, price, unix_timestamp, **data_dic)