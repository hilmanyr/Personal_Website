from django.shortcuts import render

# Create your views here.

def tampilan_home(request):
    return render(request, 'home.html', {})