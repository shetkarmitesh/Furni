
from django.urls import path
from . import views

urlpatterns = [
     path('', views.index,name="index"),
     path('about', views.about,name="about"),
     path('shop', views.shop,name="shop"),
     path('contact', views.contact,name="contact"),
     path('blog', views.blog,name="blog"),
     path('cart', views.cart,name="cart"),
     path('services', views.services,name="services"),
     path('checkout', views.checkout,name="checkout"),
     path('thankyou', views.thankyou,name="thankyou")
     
]


