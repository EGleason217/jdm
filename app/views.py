from django.shortcuts import render
from .models import *

def index(request):
    return render(request, 'index.html')

def admin(request):
    context = {
        'clients' : Clients.objects.all()
    }
    return render(request, 'admin.html', context)

# def pictureup(request):
#     if request.method == 'POST':
#         form = 
#     return render(request, )

def booking(request):
    return render(request,'order.html')

def order(request):
    if request.method == "POST":
        new_client = Clients.objects.create(name= request.POST['name'], phone= request.POST['phone'], email= request.POST['email'])
        return render(request,'admin.html')
