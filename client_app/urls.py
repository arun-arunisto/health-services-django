from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('care_portal/', care_portal, name="care_portal")
]