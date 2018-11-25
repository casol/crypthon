from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import dateparse

from .models import Profile
from .forms import RegisterForm, ProfileVerificationForm
from crypthon.settings.base import COINAPI_KEY
from clientAPI.services import Client, ClientCryptoCompare
from clientAPI.tasks import send_api_request_usd
from clientAPI.models import CryptoCurrency, CurrencyTrendingInfo, FiatCurrency

def index(request):
    """View function for home page of the site."""
    return render(request, 'account/start_page.html')


@login_required
def dashboard(request):
    """View the dashboard for logged users."""

    latest = CryptoCurrency.objects.latest('last_update')
    #latest = CryptoCurrency.objects.filter(fiatcurrency__currency='USD').last()

    #######
    fiat = FiatCurrency.objects.get(crypto_currency=latest).currency
    price = latest.price
    trending_info = CurrencyTrendingInfo.objects.get(crypto_currency=latest)
    trending_info_dic = {
        'low24hour': trending_info.low24hour,
        'high24hour': trending_info.high24hour,
        'change24hour': trending_info.change24hour,
        'changepctday': trending_info.changepctday,
        'lastvolume': trending_info.lastvolume}
    # TODO iterate over a dict
    changepctday = CurrencyTrendingInfo.objects.get(crypto_currency=latest).changepctday
    high24hour = CurrencyTrendingInfo.objects.get(crypto_currency=latest).high24hour
    low24hour = CurrencyTrendingInfo.objects.get(crypto_currency=latest).low24hour
    change24hour = CurrencyTrendingInfo.objects.get(crypto_currency=latest).change24hour
    lastvolume = CurrencyTrendingInfo.objects.get(crypto_currency=latest).lastvolume
    return render(request,
                  'account/index.html',
                  {'section': 'dashboard',
                   'price': price,
                   'fiat': fiat,
                   'trending_info_dic': trending_info_dic
                   })


def register(request):
    """Register new users and create the user profile."""
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Create a new user object but do not save it yet
            new_user = form.save(commit=False)
            # Set password
            new_user.set_password(form.cleaned_data['password1'])
            # Save the User object
            new_user.save()
            # Create the user profile
            profile = Profile.objects.create(user=new_user)
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
    else:
        form = RegisterForm()
    return render(request,
                  'account/register.html',
                  {'form':form})


@login_required
def verification(request):
    """User identity verification."""
    # check if profile is verified 
    profile_verified = request.user.profile.verified
    if request.method == 'POST':
        verification_form = ProfileVerificationForm(instance=request.user.profile,
                                                    data=request.POST,
                                                    files=request.FILES)
        if verification_form.is_valid():
            verification_form.save()
            return render(request,
                          'account/verification_done.html')
    else:
        verification_form = ProfileVerificationForm(instance=request.user.profile)
    return render(request,
                  'account/verification.html',
                  {'verification_form': verification_form,
                  'profile_verified': profile_verified})