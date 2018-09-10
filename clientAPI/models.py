from django.db import models

# Create your models here.

class OHLCV_Currency_Data(models.Model):

    """OHLCV data primary purpose is to present an overview of the market
    in human readable form. It’s used to visualize market data on chart.
    """
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