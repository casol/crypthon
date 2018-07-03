from django.db import models
from django.conf import settings

import uuid


class Wallet(models.Model):

    """A cryptocurrency wallet stores the public and private keys which
     can be used to store, receive or spend the cryptocurrency.
     """

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    id = models.AutoField(primary_key=True,)  # A private identifier
    uid = models.UUIDField(unique=True, editable=False,
                           default=uuid.uuid4, verbose_name='Public identifier',)  # A public id
    currency = models.ForeignKey('Currency', on_delete=models.PROTECT)
    # max digits? There will be ~21mln of btc, 84mln of ltc but what with xrp or something else?
    balance = models.DecimalField(max_digits=18, decimal_places=8,
                                  default=0)
    modified = models.DateTimeField(blank=True)

    class Meta:
        verbose_name = 'Wallet'
        verbose_name_plural = 'Wallets'



class Currency(models.Model):
    pass