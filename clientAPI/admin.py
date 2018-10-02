from django.contrib import admin
from .models import Crypto_Currency, Currency_Trending_Info, Fiat_Currency


class Fiat_CurrencyInline(admin.TabularInline):
    """Inline configuration for Django's admin on the Ingredient model."""
    model = Fiat_Currency
    # determined number of “extra” blank forms to fill out
    extra = 1

class Currency_Trending_InfoInline(admin.StackedInline):
    """Inline configuration for Django's admin on the Ingredient model."""
    model = Currency_Trending_Info
    extra = 1


@admin.register(Crypto_Currency)
class Crypt_Currency_admin(admin.ModelAdmin):
    """Configuration for Django's admin on the Crypto Currency model."""
    inlines = [
        Fiat_CurrencyInline,
        Currency_Trending_InfoInline,
    ]

#admin.site.register(Crypto_Currency, Crypt_Currency_admin)

