from django.urls import path
from .views import *

urlpatterns = [
    path('staff_login/', staff_login, name='staff_login')
]