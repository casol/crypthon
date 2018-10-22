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
class CryptCurrencyAdmin(admin.ModelAdmin):
    """Configuration for Django's admin on the Crypto Currency model."""
    list_display = ('crypto_currency', 'price', 'last_update', 'unix_timestamp', 'fiatcurrency__currency')
    inlines = [
        FiatCurrencyInline,
        CurrencyTrendingInfoInline,
    ]
    readonly_fields = ('last_update',)
    list_filter = ('crypto_currency', 'last_update')

    def fiatcurrency__currency(self, object):
        return object.fiatcurrency.currency


#admin.site.register(CryptoCurrency, Crypt_Currency_admin)

