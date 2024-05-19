from django.urls import path
from .views import *

urlpatterns = [
    path('agency_login/', agency_login, name="agency_login")
]