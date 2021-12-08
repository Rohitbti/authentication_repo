from django.contrib import admin
from .models import MyUser
from django.contrib.auth.admin import UserAdmin
from . import forms

class MyUserAdmin(UserAdmin):
    model = MyUser
    list_display = ['username','email','first_name','last_name', 'mobile_number','is_superuser']
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('mobile_number',)}),
    ) 
admin.site.register(MyUser,MyUserAdmin)
