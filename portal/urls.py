from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *


app_name='portal'

urlpatterns = [
    path('', index_view, name='dashboard'),
    path('today/', reports_today_view, name='reports_today'),
    path('archive/', reports_archive_view, name='archive'),
    path('login/', LoginView.as_view(template_name="portal/login.html"), name='login'),
    path('logout/', LogoutView.as_view(template_name="portal/logout.html"), name='logout'),
]