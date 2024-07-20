from django.shortcuts import render
from django.http import HttpResponse
from .models import furniture,Team_Members
# //importing models
# Create your views here.

def index(request):
    # f1= furniture()
    # f1.id=1
    # f1.name="Nordic Chair"
    # f1.prise=50.00
    # f1.img = 'product-1.png'

    # f2= furniture()
    # f2.id=2
    # f2.name="Kruzo Aero Chair"
    # f2.prise=78.00
    # f2.img = 'product-2.png'

    # f3= furniture()
    # f3.id=3
    # f3.name="Ergonomic Chair"
    # f3.prise=43.00
    # f3.img = 'product-3.png'
    # furni = [f1,f2,f3]
    # # passing the data to website 
    # return render(request,'index.html',{'furni':furni})

    furni= furniture.objects.all()
    team_members = Team_Members.objects.all()

    return render(request,'index.html',{'furni':furni,'team_members':team_members})
def login(request):
    return render (request,'login.html')

def register(request):
    return render (request,'register.html')
def about(request):
    team_members = Team_Members.objects.all()
    return render(request,'about.html',{'team_members':team_members})

def shop(request):
    furni= furniture.objects.all()
    return render(request,'shop.html',{'furni':furni})

def services(request):
    furni= furniture.objects.all()
    team_members = Team_Members.objects.all()

    return render(request,'services.html',{'furni':furni,'team_members':team_members})

def blog(request):
    team_members = Team_Members.objects.all()

    return render(request,'blog.html',{'team_members':team_members})

def contact(request):
    return render(request,'contact.html')
def cart(request):
    return render(request,'cart.html')
def checkout(request):
    return render(request,'checkout.html')
def thankyou(request):
    return render(request,'thankyou.html')

