from django.contrib import admin

# Register your models here.
from .models import furniture,Team_Members,Cart_Item
# it will add the options to add furniture from admin portal
admin.site.register(furniture)
admin.site.register(Team_Members)
admin.site.register(Cart_Item)