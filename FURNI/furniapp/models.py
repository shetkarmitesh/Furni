from django.db import models

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

# class User(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.CharField(max_length=100)
#     username = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
