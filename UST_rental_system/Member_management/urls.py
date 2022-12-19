from django.urls import path
from . import views

app_name = 'member_management'

urlpatterns = [
    path('m_sm_search/',views.search_member, name='m_sm_search'),
] 
