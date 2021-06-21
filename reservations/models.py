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
    Payment_STATUS = ( 
    ("1", "Pending"), 
    ("2", "Paid"),
    ("3", "Due"),      
    ("4", "Canceled"),      
    ) 
    Police_verification_STATUS = ( 
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
    amount = models.IntegerField(null=True)
    payment_number=models.CharField(max_length=20, null=True)
    trxid=models.CharField(max_length=250, null=True)
    paymentStatus=models.CharField(choices=Payment_STATUS, max_length=15, default="Pending")
    nid = models.IntegerField(null=True)
    nationality = models.CharField(max_length=250, null=True)
    marital_status = models.CharField(max_length=250, null=True)
    father_name = models.CharField(max_length=250, null=True)
    mother_name = models.CharField(max_length=250, null=True)
    policeStatus=models.CharField(choices=Police_verification_STATUS, max_length=15, default="Pending")

    def __str__(self):
        return self.flat.flatnumber
    


