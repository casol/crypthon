from django.contrib import admin
from .models import CryptoCurrency, CurrencyTrendingInfo, FiatCurrency


class FiatCurrencyInline(admin.TabularInline):
    """Inline configuration for Django's admin on the Ingredient model."""
    model = FiatCurrency
    # determined number of “extra” blank forms to fill out
    extra = 0

class CurrencyTrendingInfoInline(admin.StackedInline):
    """Inline configuration for Django's admin on the Ingredient model."""
    model = CurrencyTrendingInfo
    extra = 0


@admin.register(CryptoCurrency)
class Crypt_Currency_admin(admin.ModelAdmin):
    """Configuration for Django's admin on the Crypto Currency model."""
    inlines = [
        FiatCurrencyInline,
        CurrencyTrendingInfoInline,
    ]

#admin.site.register(CryptoCurrency, Crypt_Currency_admin)

