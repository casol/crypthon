from django.shortcuts import render
from django.contrib.auth.decorators import login_required
#from .forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm

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
            form.save()
            username = form.cleaned_data.get('username')
            raw_passoword = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'account/register.html', {'form':form})
