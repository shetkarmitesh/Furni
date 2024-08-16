from django.db import models
import datetime 
import uuid
from django.contrib.auth.models import User
# Create your models here.

# class furniture:
#     id : int
#     prise : float
#     name : str
#     img : str

class furniture(models.Model):
    name = models.CharField (max_length=100)
    # img would be upload it will not stored in database so we have to path here to access
    img = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    
class Team_Members(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    ExecutiveTestimonials = models.CharField(max_length=300,null=True)
    img = models.ImageField(upload_to='team_members')

class Cart_Item(models.Model):
    product = models.ForeignKey(furniture,on_delete=models.CASCADE,default=1) 
    customer = models.ForeignKey(User, on_delete=models.CASCADE,default=1) 
    quantity = models.IntegerField(default=1) 
    productName = models.CharField (max_length=100,default="")
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    img = models.ImageField(upload_to='orders')
    date = models.DateField(default=datetime.datetime.today) 
    total = models.FloatField(default = 0.0)
    # totalAmount = models.FloatField(default = 0.0)        
    def __str__(self):
        # return f'{self.customer} | {self.quantity} x {self.productName}'
        return f'{self.customer}'

class Orders(models.Model):
    class statsType (models.TextChoices):
        Pending = 'Pending'
        Placed = 'Placed'
        Delivered = 'Delivered'

    order_id = models.CharField(max_length=36)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12,default=0.00,decimal_places=2)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    streetAddress = models.CharField(max_length=100)
    optionalAddress = models.CharField(max_length=100)
    Country = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phoneNo = models.IntegerField()
    posta_Zip = models.CharField(max_length=50)
    OrderNotes = models.CharField(max_length=500)
    status = models.CharField(max_length=10,choices=statsType.choices,default=statsType.Pending) 
  
    ProductName = models.CharField(max_length=100,default="")
    price = models.IntegerField()
    quantity = models.IntegerField(default=1) 
    total = models.FloatField(default = 0.0)

class ContactUs(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    message  = models.CharField(max_length=500)
    