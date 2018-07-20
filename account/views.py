from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Profile
from .forms import RegisterForm, ProfileVerificationForm
from crypthon.settings.base import COINAPI_KEY
from clientAPI.services import Client


def index(request):
    """View function for home page of the site."""
    return render(request, 'account/start_page.html')


@login_required
def dashboard(request):
    """View the dashboard for logged users."""
    client = Client(COINAPI_KEY)
    response = client.get_specific_rate(currency_pair='LTC/USD').json()
    json = response['rate']

    return render(request,
                  'account/index.html',
                  {'section': 'dashboard',
                   'json': json})


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