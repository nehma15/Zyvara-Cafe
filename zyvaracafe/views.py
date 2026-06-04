from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'homepage.html')


def about(request):
    return render(request,'aboutpage.html')


def cakes(request):
    return render(request,'cakes.html')


def menu(request):
    return render(request,'menu.html')


def reservation(request):
    return render(request,'reservation.html')


def contact(request):
    return render(request,'contact.html')


