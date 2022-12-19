from django.urls import path
from . import views

app_name = 'ES_management'
urlpatterns = [
    path('add_equ/', views.add_equ, name='add_equ'),
    path('update_equ/', views.update_equ, name='update_equ'),
    
]