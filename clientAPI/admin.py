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
    list_display = ('crypto_currency', 'price', 'fiatcurrency',
                    'last_update',)
    inlines = [
        FiatCurrencyInline,
        CurrencyTrendingInfoInline,
    ]
    readonly_fields = ('last_update',)
    list_filter = ('crypto_currency', 'last_update',)

    def fiatcurrency(self, obj):
        return FiatCurrency.objects.get(crypto_currency=obj)


#admin.site.register(CryptoCurrency, Crypt_Currency_admin)

