from django.shortcuts import render

# Create your views here.
def agency_login(request):
    return render(request, "agency_app/agency_login.html")