from django.urls import path
from .views import *


app_name='portal'

urlpatterns = [
    path('', index_view, name='index'),
    # path('login/', )
]