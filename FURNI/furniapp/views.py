from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import furniture,Team_Members
from django.contrib.auth.models import User,auth
from django.contrib import messages

# pagination
from django.core.paginator import Paginator

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

def contactUs(request):
    return render(request,'contact.html')

def cart(request):
    return render(request,'cart.html')
def checkout(request):
    return render(request,'checkout.html')
def thankyou(request):
    return render(request,'thankyou.html')

def logout (request):
    auth.logout(request)
    return render(request,'index.html')
def login(request):
    if request.method=="POST":
        # fetching the data from form
        username = request.POST['username']
        password = request.POST['pwd']
        user = auth.authenticate(username=username ,password=password)
        if user is not None: 
            auth.login(request,user)
            return redirect('/')
        else: 
            messages.info(request,"invalid credentails")
            redirect('login')
    return render (request,'login.html')


def register(request):
    if request.method=="POST":
        # fetching the data from form
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['pwd1']
        password2= request.POST['pwd2']

        # adding the data to database
        if password1==password2:
            if User.objects.filter(username=username).exists():
                # print("username taknen ")
                messages.info(request, "The username is taken")
                # return render(request,'register.html')
                return redirect('register')
                
            elif User.objects.filter(email=email).exists():
                # print("user already exists")
                messages.info(request, "The user is alredy taken")
                return redirect('register')

                # return render(request,'register.html')

            user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
            user.save()
            # print("user created successfully***********")
            # messages.info(request, "user created successfully")
            return redirect('login')
        else: 
            # print("password not matching")
            messages.info(request, "password not matching")
            return redirect('register')

    else:
        return render(request,'register.html') 


def addToCart(request,id):
    

    return redirect('shop')



# def listing(request):
#     contact_list = furniture.objects.all()
#     paginator = Paginator(contact_list, 4)  # Show 25 contacts per page.

#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)
#     return render(request, "try.html", {"page_obj": page_obj,'furni':contact_list})
    
# # def try1(request):
# #     return render(request,"try.html")