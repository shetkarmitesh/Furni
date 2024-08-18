from math import ceil
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from .models import furniture,Team_Members,Cart_Item,Orders,ContactUs,ShopDetails
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import uuid
# pagination
from django.core.paginator import Paginator
# to display alerts
import sweetify
# //importing models
# Create your views here.

def index(request):
    
    furni= furniture.objects.all()
    n= len(furni)
    n_slides= n//4*ceil(n/4)-(n//4)
    cart_details = Cart_Item.objects.all().filter(customer_id=request.user.id)

    team_members = Team_Members.objects.all()

    return render(request,'index.html',{'furni':furni,'team_members':team_members,'no_slides':n_slides,'range':range(n_slides),'cartItem':len(cart_details)})


def about(request):
    team_members = Team_Members.objects.all()
    cart_details = Cart_Item.objects.all().filter(customer_id=request.user.id)
    return render(request,'about.html',{'team_members':team_members,'cartItem':len(cart_details)})

def shop(request):
    furni= furniture.objects.all()
    cart_details = Cart_Item.objects.all().filter(customer_id=request.user.id)
    return render(request,'shop.html',{'furni':furni,'cartItem':len(cart_details)})

def services(request):
    furni= furniture.objects.all()
    cart_details = Cart_Item.objects.all().filter(customer_id=request.user.id)
    team_members = Team_Members.objects.all()

    return render(request,'services.html',{'furni':furni,'team_members':team_members,'cartItem':len(cart_details)})

def blog(request):
    team_members = Team_Members.objects.all()
    cart_details = Cart_Item.objects.all().filter(customer_id=request.user.id)
    return render(request,'blog.html',{'team_members':team_members,'cartItem':len(cart_details)})





def logout (request):
    del request.session["member_id"]
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
            request.session["member_id"] = request.user.id
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
        sweetify.success(request, 'Item Added', timer=1000)
    else:
        # Update existing cart item quantity
        cart_item = Cart_Item.objects.get(product_id=product_id,customer=request.user)
        cart_item.quantity+=1
        cart_item.total = price*cart_item.quantity
        # print(quantity)
        cart_item.save()
        sweetify.success(request, 'Item Added', timer=1000)

    return redirect('shop')
@login_required
def cart(request):
    cart_details = Cart_Item.objects.all().filter(customer_id=request.user.id)
    total_cart_price=0
    for i in cart_details : 
        total_cart_price = i.total + total_cart_price
    cart_details.totalAmount = total_cart_price
    return render(request,'cart.html',{'cart_details':cart_details,'total_cart_price':total_cart_price,'cartItem':len(cart_details)})
@login_required
def remove_cart_item(request):
    if request.method =="POST":
        prod_id = int(request.POST.get('product_id'))
        # print(prod_id,"asdasdhkjadshakjdsa")

        cart_item = Cart_Item.objects.filter(id=prod_id, customer=request.user)
        if cart_item.exists() :

            cart_item.delete()
            pass
       
        # sweetify.success(request, 'Item Deleted', timer=1000)
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
    if len(cart_details)<=0:
        sweetify.success(request, 'Your Amazon Cart is empty',button='ok')
        return redirect("/shop")
    # user = User.objects.get(id=request.user.id)
    total_cart_price=0.0
    for i in cart_details : 
        total_cart_price = i.total + total_cart_price
   
    return render(request,'checkout.html',{'cart_details':cart_details,'total_cart_price':total_cart_price,'cartItem':len(cart_details)})

def thankyou(request):
    if request.method == "POST":
        
        first_name = str(request.POST['c_fname'])
        last_name = str(request.POST['c_lname'])
        address = request.POST['c_address']
        addressOptional = request.POST['c_addressOptional']
        state = request.POST['c_state_country']
        posta = request.POST['c_postal_zip']
        email = request.POST['c_email_address']
        orderNotes = request.POST['c_order_notes']
        phoneNo = int(request.POST['c_phone'])
        totalAmount = float(request.POST['c_order_total'])

        cart_details = Cart_Item.objects.all().filter(customer_id=request.user.id)
        order_id = str(uuid.uuid4()) 
        # print(order_id,"sdfsagfghtedssghsterefs")
        for cart in cart_details:
            order= Orders.objects.create(
                        order_id=order_id,
                        user=request.user,
                        amount= totalAmount,
                        first_name = first_name,
                        last_name = last_name,
                        streetAddress =address,
                        optionalAddress =addressOptional,
                        Country =state,
                        email =email,
                        phoneNo =phoneNo,
                        posta_Zip =posta,
                        OrderNotes =orderNotes,
                        status = 'Placed',

                        price = cart.price,
                        ProductName = cart.productName,
                        quantity=cart.quantity,
                        total=cart.total,
                    )
            order.save()
        cart_details.delete()
    return render(request,'thankyou.html',{'cartItem':len(cart_details)})


def contactUs(request):
    if request.method == "POST":
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        messages = request.POST['message']
        contactUs= ContactUs.objects.create(
            first_name = first_name,  
            last_name = last_name, 
            email= email,
            message = messages)
        contactUs.save()
        sweetify.success(request, 'Send Succefully', timer=1000)
        return redirect('contactUs')
    cart_details = Cart_Item.objects.all().filter(customer_id=request.user.id)
    shopDetails = ShopDetails.objects.get(id = 1)

    return render(request,'contact.html',{'cartItem':len(cart_details),'shopDetails':shopDetails}) 