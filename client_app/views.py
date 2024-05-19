from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "client_app/index.html")

def care_portal(request):
    return render(request, "client_app/care_portal.html")

