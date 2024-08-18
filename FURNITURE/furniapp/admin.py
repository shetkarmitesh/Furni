from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.
from .models import furniture,Team_Members,Cart_Item,ContactUs,ShopDetails,CustomUser
# it will add the options to add furniture from admin portal
admin.site.register(furniture)
admin.site.register(Team_Members)
admin.site.register(Cart_Item)
admin.site.register(ContactUs)
admin.site.register(ShopDetails)

class UserAdmin(BaseUserAdmin):
    model = CustomUser
    # Add fields to be displayed in the admin
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'birth_date', 'profile_picture','phoneNo','subscriberOfNewsletter')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'birth_date', 'profile_picture'),
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'birth_date', 'is_staff','subscriberOfNewsletter','phoneNo')
    search_fields = ('username', 'email')
    ordering = ('username',)

admin.site.register(CustomUser, UserAdmin)