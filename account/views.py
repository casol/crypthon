from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm


def index(request):
    """View function for home page of site."""
    return render(request, 'account/index.html')


@login_required
def dashboard(request):
    """View the dashboard for logged users."""
    return render(request,
                  'account/dashboard.html',
                  {'section': 'dashboard'})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Create a new user object but do not save it yet
            new_user = form.save(commit=False)
            # Set password
            new_user.set_password(form.cleaned_data['password1'])
            # Save the User object
            new_user.save()
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
    else:
        form = RegisterForm()
    return render(request,
                  'account/register.html',
                  {'form':form})
