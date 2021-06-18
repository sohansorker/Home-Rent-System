from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = CustomUser
    list_display = ['pk', 'email', 'username', 'first_name', 'last_name']
    add_fieldsets = UserAdmin.add_fieldsets + (
    (None, {'fields': ('email', 'first_name', 'last_name', 'date_of_birth', 'address1', 'zip_code', 'city', 'country', 'mobile_phone', 'photo',)}),
)
    fieldsets = UserAdmin.fieldsets + (
    (None, {'fields': ( 'date_of_birth', 'address1',  'zip_code', 'city', 'country', 'mobile_phone', 'photo',)}),
)


admin.site.register(CustomUser, CustomUserAdmin)