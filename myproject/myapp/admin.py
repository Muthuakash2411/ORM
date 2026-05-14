from django.contrib import admin
from .models import food
# Register your models here.
class foodAdmin(admin.ModelAdmin):
    list_display=('orderid','Itemname','OrderQty','TotalAmount','Delivery_Address')
admin.site.register(food)