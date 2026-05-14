# Ex01 Django ORM Web Application
## Date: 14-05-2026

## AIM
To develop a Django application to manage an online food delivery platform like Zomato/Swiggy using Object Relational Mapping (ORM).

## ENTITY RELATIONSHIP DIAGRAM



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM

# Models.py
````
from django.db import models

# Create your models here.
class food(models.Model):
    orderid=models.IntegerField(primary_key=True)
    Itemname=models.CharField(max_length=20)
    OrderQty=models.IntegerField()
    TotalAmount=models.FloatField()
    Delivery_Address=models.CharField(max_length=100)
````

## Admin.py
````
from django.contrib import admin
from .models import food
# Register your models here.
class foodAdmin(admin.ModelAdmin):
    list_display=('orderid','Itemname','OrderQty','TotalAmount','Delivery_Address')
admin.site.register(food)

````
## OUTPUT

Include the screenshot of your admin page.


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
