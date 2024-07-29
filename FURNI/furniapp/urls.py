
from django.urls import path
from . import views

urlpatterns = [
     path('', views.index,name="index"),
     path('about', views.about,name="about"),
     path('shop', views.shop,name="shop"),
     path('contactUs', views.contactUs,name="contactUs"),
    
     path('blog', views.blog,name="blog"),
     path('cart', views.cart,name="cart"),
     path('services', views.services,name="services"),
     path('checkout', views.checkout,name="checkout"),
     path('thankyou', views.thankyou,name="thankyou"),
     path('register', views.register,name="register"),
     path('login', views.login,name="login"),
     path('logout', views.logout,name="logout"),
     # path('asd', views.asd,name="asd"),

     path ('addToCart',views.addToCart,name='addToCart')
     # path ('try',views.try1,name='try'),
     # path ('listing',views.listing,name='listing'),
     

]


