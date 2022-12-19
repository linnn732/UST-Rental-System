from django.urls import path
from . import views

app_name = 'member'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('m_nu_edit/', views.edit_member, name='m_nu_edit'),
    path('m_se_edit/', views.edit_member, name='m_se_edit'),
    path('m_sm_edit/', views.edit_member, name='m_sm_edit'),
]