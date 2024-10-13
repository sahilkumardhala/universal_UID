from django.db import models
# from django.contrib.auth.models import User
import random
# Create your models here.
def unique_user_UID():
            prefix = "UID"
            while True:
                random_number = random.randint(1000, 9999)  # Generate a random number of 4 digits
                UID = f"{prefix}{random_number}"
                if not UIDmodel.objects.filter(UID=UID).exists():
                    return UID
                
class UIDmodel(models.Model):
    # user = models.ForeignKey(User, on_delete = models.SET_NULL,null=True, blank=True)

    username=models.CharField(max_length=60)
    phno=models.IntegerField()
    email=models.EmailField(max_length=100)

    
    UID = models.CharField(max_length=7, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.UID:  # If UID is not already set
            self.UID = unique_user_UID()
        super(UIDmodel, self).save(*args, **kwargs)


    password=models.CharField(max_length=5,default="Welcome")