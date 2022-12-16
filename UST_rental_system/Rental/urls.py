from django.urls import path
from . import views

app_name = 'rental'
urlpatterns = [
    path('search_nu_site/', views.search_nu_site, name='search_nu_site'),
    #path('login/', views.login, name='login')
]