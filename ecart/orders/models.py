from django.db import models
from customers.models import Customer
from product.models import Product
# model for order

class Order(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))

    CART_STAGE=0
    ORDER_CONFIRMED=1
    ORDER_PROCESSED=2
    ORDER_REJECTED=4
    ORDER_DELIVERED=3
    STATUS_CHOICE=((ORDER_PROCESSED,'ORDER_PROCESSED'),
                   (ORDER_CONFIRMED,'ORDER_CONFIRMED'),
                   (ORDER_REJECTED,'ORDER_REJECTED'),
                   (ORDER_DELIVERED,'ORDER_DELIVERED'))

    order_status=models.IntegerField(choices=STATUS_CHOICE,default=CART_STAGE)
    owner=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,related_name='orders')
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
class Ordered_Item(models.Model):
    product=models.ForeignKey(Product,related_name='added_cart',on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField(default=1)
    owner=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='ordered_item')

