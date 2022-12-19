from django.urls import path
from . import views

app_name = 'order_management'
urlpatterns = [
    path('e_se_search/', views.search_se_equ, name='e_se_search'),
    path('generate_rental_e_se/', views.generate_rental_equ, name='generate_rental_e_se'),
]