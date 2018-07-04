from django.db import models
from django.conf import settings

import uuid


class Wallet(models.Model):

    """A cryptocurrency wallet stores the public and private keys which
     can be used to store, receive or spend the cryptocurrency.
     """

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    currency = models.ForeignKey('Currency', on_delete=models.PROTECT)
    # max digits? There will be ~21mln of btc, 84mln of ltc but what with xrp or something else?
    balance = models.DecimalField(max_digits=18, decimal_places=8,
                                  default=0)
    created = models.DateTimeField(blank=True)
    modified = models.DateTimeField(blank=True)
    active = models.BooleanField(default=False)
    transaction_counter = models.IntegerField(default=1)

    class Meta:
        verbose_name = 'Wallet'
        verbose_name_plural = 'Wallets'



class Currency(models.Model):
    pass

class Address(models.Model):
    """
    In simple terms a wallet address is similar to a bank account number.
    It’s a unique 26-35 digit combination of letters and numbers and it
    looks something like this: 1ExAmpLe0FaBiTco1NADr3sSV5tsGaMF6hd
    """
    pass

class Action(models.Model):
    pass