from django.urls import path
from .views import *


app_name='portal'

urlpatterns = [
    path('', index_view, name='dashboard'),
    path('today/', reports_today_view, name='reports_today'),
    path('archive/', reports_archive_view, name='archive')
]