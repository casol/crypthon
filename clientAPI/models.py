from django.db import models

# Create your models here.
"""
class OHLCV_Currency_Data(models.Model):

    OHLCV data primary purpose is to present an overview of the market
    in human readable form. It’s used to visualize market data on chart.
    
    time_period_start = models.DateTimeField(editable=False, null=False, blank=False)
    time_period_end = models.DateTimeField(editable=False, null=False, blank=False)
    time_open = models.DateTimeField(editable=False, null=False, blank=False)
    time_close = models.DateTimeField(editable=False, null=False, blank=False)
    price_open = models.DecimalField(max_digits=18, decimal_places=9)
    price_high = models.DecimalField(max_digits=18, decimal_places=9)
    price_low = models.DecimalField(max_digits=18, decimal_places=9)
    price_close = models.DecimalField(max_digits=18, decimal_places=9)
    volume_trade = models.DecimalField(max_digits=19, decimal_places=10)
    trades_count = models.IntegerField(blank=True)
"""


class Crypto_Currency(models.Model):
    """Returns a market's last price."""

    BITCOIN = 'BTC'
    ETHEREUM = 'ETH'
    LITECOIN = 'LTC'
    RIPPLE = 'XRP'
    CRYPTO_CURRENCY_CHOICES = (
        (BITCOIN, 'Bitcoin'),
        (ETHEREUM, 'Ethereum'),
        (LITECOIN, 'Litecoin'),
        (RIPPLE, 'RIPPLE'),
    )

    crypto_currency = models.CharField(max_length=50, blank=True, null=False,
                                       choices=CRYPTO_CURRENCY_CHOICES)
    price = models.DecimalField(max_digits=18, decimal_places=9, null=True, blank=True)
    last_update = models.DateTimeField(auto_now_add=True)
    unix_timestamp = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['-last_update']
        verbose_name = 'cryptocurrency'
        verbose_name_plural = 'cryptocurrencies'


    def __str__(self):
        return self.crypto_currency


class Fiat_Currency(models.Model):
    """Fiat currency available for trending."""

    DOLLAR = 'USD'
    EURO = 'EUR'
    FIAT_CURRENCY_CHOICES = (
        (DOLLAR, 'Dollar'),
        (EURO, 'Euro'),
    )
    crypto_currency = models.ForeignKey(Crypto_Currency, on_delete=models.CASCADE)
    currency = models.CharField(max_length=50, blank=True, null=False,
                                choices=FIAT_CURRENCY_CHOICES)
    class Meta:
        verbose_name = 'fiat currency'
        verbose_name_plural = 'fiat currencies'

    def __str__(self):
        return self.currency


class Currency_Trending_Info(models.Model):
    """Stores a market's last price as well as other stats based on a 24-hour sliding window."""

    crypto_currency = models.ForeignKey(Crypto_Currency, on_delete=models.CASCADE)
    market = models.CharField(max_length=30, blank=True, null=False)
    lastvolume = models.DecimalField(max_digits=18, decimal_places=9, null=True)
    lastvolumeto = models.DecimalField(max_digits=18, decimal_places=9, null=True)
    lasttradeid = models.BigIntegerField(null=True)
    openday = models.DecimalField(max_digits=18, decimal_places=9, null=True, blank=True)
    highday = models.DecimalField(max_digits=18, decimal_places=9, null=True, blank=True)
    lowday = models.DecimalField(max_digits=18, decimal_places=9, null=True, blank=True)
    open24hour = models.DecimalField(max_digits=18, decimal_places=9, null=True, blank=True)
    high24hour = models.DecimalField(max_digits=18, decimal_places=9, null=True, blank=True)
    low24hour = models.DecimalField(max_digits=18, decimal_places=9, null=True, blank=True)
    change24hour = models.DecimalField(max_digits=18, decimal_places=9, null=True, blank=True)
    changepct24hour = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    changeday = models.DecimalField(max_digits=18, null=True, blank=True, decimal_places=9)
    changepctday = models.DecimalField(max_digits=18, null=True, blank=True, decimal_places=9)
    supply = models.IntegerField()
    mktcap = models.BigIntegerField(null=True, blank=True)

    #class Meta:
        #ordering = ['-last_update']

    def __str__(self):
        return 'Open: {}, High: {}, Low: {}'.format(self.openday, self.highday, self.lowday)