from django.shortcuts import render

def static_landing(request):
    return render(request, 'landing.html')
# Create your views here.

def contact_landing(request):
    return render(request, 'contacto.html')