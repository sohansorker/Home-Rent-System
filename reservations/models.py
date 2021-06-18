from django.db import models
from flats.models import Flat
from accounts.models import CustomUser
from month.models import MonthField

# Create your models here.
class Reservation(models.Model):
    Reservation_STATUS = ( 
    ("1", "Pending"), 
    ("2", "Approved"),
    ("3", "Canceled"),      
    ) 
    id = models.AutoField(primary_key=True)
    status=models.CharField(choices=Reservation_STATUS, max_length=15, default="Pending")
    check_in = MonthField("Month Value", help_text="some help...")
    check_out = MonthField("Month Value", help_text="some help...")
    flat = models.ForeignKey(Flat, on_delete = models.CASCADE)
    guest = models.ForeignKey(CustomUser, on_delete= models.CASCADE)
    payment_number=models.CharField(max_length=20)
    trnxid=models.CharField(max_length=250)
    booking_id = models.CharField(max_length=100,default="null")

    def __str__(self):
        return self.guest.username
