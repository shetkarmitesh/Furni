
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
     path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'), 
     path('remove_cart_item/<int:cart_id>/', views.remove_cart_item, name='remove_cart_item'), 
     path('update_cart_item/<int:cart_id>/<int:quantity>/',views.update_cart_item, name='update_cart_item'), 

]


