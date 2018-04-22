from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def index(request):
    """View function for home page of site."""
    return render(request, 'account/index.html')


@login_required
def dashboard(request):
    """View the dashboard for logged users."""
    return render(request,
                  'account/dashboard.html',
                  {'section': 'dashboard'})