from django.db import models
from accounts.models import CustomUser

# Create your models here.
class House(models.Model):
    #h_id,h_name,owner ,location,rooms
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30,null=True)
    owner = models.ForeignKey(CustomUser, blank=True, null=True, on_delete=models.CASCADE)
    location = models.CharField(max_length=50)
    state = models.CharField(max_length=50,null=True)
    zipcode = models.CharField(max_length=50,null=True)
    country = models.CharField(max_length=50,null=True)
    photo=models.ImageField(upload_to='hotel/', null=True, blank=True)


    def __str__(self):
        return self.name