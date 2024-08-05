from django.db import models
import datetime 
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
    address = models.CharField(max_length=50, default='', blank=True) 
    phone = models.CharField(max_length=50, default='', blank=True) 
    date = models.DateField(default=datetime.datetime.today) 
    status = models.BooleanField(default=False) 
    total = models.FloatField(default = 0.0)
    def __str__(self):
        # return f'{self.customer} | {self.quantity} x {self.productName}'
        return f'{self.customer}'


