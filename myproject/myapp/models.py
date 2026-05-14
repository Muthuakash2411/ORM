from django.db import models

# Create your models here.
class food(models.Model):
    orderid=models.IntegerField(primary_key=True)
    Itemname=models.CharField(max_length=20)
    OrderQty=models.IntegerField()
    TotalAmount=models.FloatField()
    Delivery_Address=models.CharField(max_length=100)