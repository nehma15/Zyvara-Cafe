from django.shortcuts import render,get_object_or_404
from .models import Cake 

# Create your views here.

def home(request):
    return render(request,'homepage.html')


def about(request):
    return render(request,'aboutpage.html')


# celebration cake 
def cakes_list(request):
    cakes = Cake.objects.all()
    return render(request, 'cakes.html', {'cakes': cakes})


def cake_detail(request, cake_id):
    cake = get_object_or_404(Cake, id=cake_id)
    return render(request, 'cake_detail.html', {'cake': cake})



def menu(request):
    return render(request,'menu.html')


def reservation(request):
    return render(request,'reservation.html')


def contact(request):
    return render(request,'contact.html')


