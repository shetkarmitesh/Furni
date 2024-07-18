from django.contrib import admin

# Register your models here.
from .models import furniture
# it will add the options to add furniture from admin portal
admin.site.register(furniture)