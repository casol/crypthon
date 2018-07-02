from django.db import models

class Wallet(models.Model):
    """"""
    currency = models.ForeignKey('Currency',
                                 on_delete=models.CASCADE,)







class Currency(models.Model):
    pass