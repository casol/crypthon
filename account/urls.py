from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    url(r'^$',
        views.index,
        name='index'),
    url(r'^market/$',
        views.dashboard,
        name='dashboard'),
    url(r'^register/$',
        views.register,
        name='register'),
    url(r'^verification/$',
        views.verification,
        name='verification'),
]