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