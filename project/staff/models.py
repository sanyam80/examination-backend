from django.db import models

# Create your models here.

class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True, unique=True)
    name= models.CharField(max_length=75)
    email=models.EmailField(unique=True)
    password=models.CharField(null=False, blank=False, max_length=75)

    def __str__(self):
        return self.name