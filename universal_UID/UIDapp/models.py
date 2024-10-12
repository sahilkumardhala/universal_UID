from django.db import models
from UIDapp.views import *
# Create your models here.
class UIDmodel(models.Model): 
    username=models.CharField(max_length=60)
    phno=models.IntegerField()
    email=models.EmailField(max_length=100)

    
    UID = models.CharField(max_length=7, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.UID:  # If UID is not already set
            self.UID = unique_user_UID()
        super(UIDmodel, self).save(*args, **kwargs)


    password=models.CharField(max_length=5,default="Welcome")