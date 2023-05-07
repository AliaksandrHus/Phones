from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('user_home', views.user_home, name='user_home'),
    path('error', views.error, name='error'),

    path('phones_all', views.phones_all, name='phones_all'),
    path('phones_7', views.phones_7, name='phones_7'),
    path('phones_985', views.phones_985, name='phones_985'),
    path('search', views.search, name='search'),

    path('login_page', views.login_page, name='login_page'),
    path('logout_page', views.logout_page, name='logout_page'),
    path('registration_page', views.registration_page, name='registration_page'),
]
