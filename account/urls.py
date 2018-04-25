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

    # auth login/logout
    url(r'^login/$',
        auth_views.login,
        name='login'),
    url(r'^logout/$',
        auth_views.logout,
        name='logout'),

    # auth change password
    url(r'^password-change/$',
        auth_views.password_change,
        name='password_change'),
    url(r'^password-change/done/$',
        auth_views.password_change_done,
        name='password_change_done'),
]