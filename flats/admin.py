from django.contrib import admin
from .models import Flat

# Register your models here.
@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    list_display=('flatnumber','status','flat_type','house','price','rent_status')