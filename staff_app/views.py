from django.shortcuts import render

# Create your views here.
def staff_login(request):
    return render(request, "staff_app/staff_login.html")
