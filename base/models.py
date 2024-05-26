
from django.db import models
# from carts.models import Cart
# from .utils import unique_order_id_generator
from django.db.models.signals import pre_save
import random
import string
# from django_countries.fields import CountryField


def id_generator(size=9, chars=string.ascii_uppercase + string.digits):
        return "TLE-"+''.join(random.choice(chars) for _ in range(size))


ORDER_STATUS_CHOICES= (
    ('Not Yet Shipped', 'Not Yet Shipped'),
    ('Shipped', 'Shipped'),
    ('Cancelled', 'Cancelled'),
    ('Refunded', 'Refunded'),
    ('Pending', 'Pending')
    )

PAYMENT_STATUS_CHOICES= (
    ('Paid', 'Paid'),
    ('Unpaid', 'Unpaid')
)

class Delivery(models.Model):
    # order_id= models.CharField(max_length=120, blank= True)
    sender_name = models.CharField(max_length=200, null=True)
    sender_address = models.CharField(max_length=200, null=True)
    sender_email = models.EmailField(null=True, blank=True)
    sender_phone = models.CharField(max_length=20)

    # Recievers Details
    receivers_name = models.CharField(max_length=200, null=True)
    receivers_email = models.EmailField(null=True, blank=True)
    receivers_phone = models.CharField(max_length=20)
    receivers_address = models.CharField(max_length=255, null=True, blank=True)
    destination_country = models.CharField(max_length=200, null=True)
    delivery_status= models.CharField(max_length=120, default='Not Yet Shipped', choices= ORDER_STATUS_CHOICES)
    payment_status = models.CharField(max_length=120, default='Unpaid', choices= PAYMENT_STATUS_CHOICES)
    
    clearance_cost = models.DecimalField(default=0.0, max_digits=10000, decimal_places=2)
    insurance = models.DecimalField(default=0.0, max_digits=10000, decimal_places=2)
    # total= models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    delivery_date = models.DateField(null=True)

    tracking_id = models.CharField(max_length=13, null=True, blank=True, unique=True) 

    

    created = models.DateField(auto_now=True)
    updated = models.DateField(auto_now_add=True)


    def __str__(self):
         return self.receivers_name
    

    class Meta:
         ordering = ['-updated', '-created']

# Sample of an ID generator - could be any string/number generator
# For a 6-char field, this one yields 2.1 billion unique IDs
    

    def save(self):
        if not self.tracking_id:
            # Generate ID once, then check the db. If exists, keep trying.
            self.tracking_id = id_generator()
            while Delivery.objects.filter(tracking_id=self.tracking_id).exists():
                self.tracking_id = id_generator()
        super(Delivery, self).save()



class Item(models.Model):
    receiver = models.ForeignKey(Delivery, on_delete=models.CASCADE, null=True)
    product_name = models.CharField(max_length=255)
    weight = models.DecimalField(default=1.0, decimal_places=2, max_digits=300)
    quantity = models.IntegerField(default=1, null=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    shipping_cost= models.DecimalField(default=0.0, max_digits=10000, decimal_places=2)


    def __str__(self):
        return self.product_name