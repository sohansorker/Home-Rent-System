from django.db import models
from houses.models import House

# Create your models here.
class Flat(models.Model):
    FLAT_STATUS = ( 
    ("1", "available"), 
    ("2", "not available"),    
    ) 

    FLAT_TYPE = ( 
    ("1", "Premium"), 
    ("2", "Deluxe"),
    ("3","Basic"),    
    ) 

    #type,no_of_rooms,capacity,prices,Hotel
    id = models.AutoField(primary_key=True)
    house= models.ForeignKey(House, on_delete = models.CASCADE)
    flat_type = models.CharField(max_length=50,choices = FLAT_TYPE)
    price = models.IntegerField()
    status = models.CharField(choices =FLAT_STATUS,max_length = 15)
    flatnumber = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    rent_status = models.BooleanField(default=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.flatnumber


