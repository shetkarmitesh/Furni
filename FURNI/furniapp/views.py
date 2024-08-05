from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from .models import furniture,Team_Members,Cart_Item
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# pagination
from django.core.paginator import Paginator
# to display alerts
import sweetify
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

@login_required
def add_to_cart(request, product_id):
    product = furniture.objects.get(id=product_id)
    quantity =1
    price = product.price
    total = quantity * price

# Check if the item already exists in the cart for the current user
    if not Cart_Item.objects.filter(product_id=product_id, customer=request.user).exists():
        # Create a new cart item if it doesn't exist
        cart_item = Cart_Item.objects.create(
                product=product,
                customer=request.user,
                quantity=quantity,
                productName=product.name,
                price=price,
                img= product.img,
                total= total
            )
        cart_item.save()
    else:
        # Update existing cart item quantity
        cart_item = Cart_Item.objects.get(id=product_id)
        cart_item.quantity+=1
        cart_item.total = price*cart_item.quantity
        # print(quantity)
        cart_item.save()

    # messages.info(request,"{} is added successfully".format(product.name))
    sweetify.success(request, 'Item Added', timer=1000)
    return redirect('shop')
@login_required
def cart(request):
    cart_details = Cart_Item.objects.all().filter(customer_id=request.user.id)
    total_cart_price=0
    for i in cart_details : 
        total_cart_price = i.total + total_cart_price
    return render(request,'cart.html',{'cart_details':cart_details,'total_cart_price':total_cart_price})
@login_required
def remove_cart_item(request,cart_id):
    cart_item = Cart_Item.objects.filter(id=cart_id, customer=request.user)
    if cart_item.exists():
        cart_item.delete()
    else:
        print("product not found ")
    sweetify.success(request, 'Item Deleted', timer=1000)
    return redirect('cart')
@login_required
def update_cart_item(request):
    if request.method =="POST":
        prod_id = int(request.POST.get('product_id'))
        prod_qty = int(request.POST.get('product_qty'))
        cart_item = Cart_Item.objects.filter(id=prod_id, customer=request.user)
       
        if cart_item.exists():
            cart_item = Cart_Item.objects.get(id=prod_id)
            cart_item.quantity= prod_qty
            cart_item.total = cart_item.price*cart_item.quantity
            cart_item.save()
            sweetify.success(request, 'Item Updated', timer=1000)
       
    return redirect('cart')



def checkout(request):
    cart_details = Cart_Item.objects.all().filter(customer_id=request.user.id)

    return render(request,'checkout.html',{'cart_details':cart_details})