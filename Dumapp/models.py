from django.db import models

# Create your models here.


class Member(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length = 50)
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.name
from django.db import models

class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100) 
    quantity = models.PositiveIntegerField(default=1)  
    description = models.TextField(max_length=500, blank=True, null=True) 
    delivery_address = models.TextField(max_length=300)  
    contact_number = models.CharField(max_length=15) 

    def __str__(self):
        return f"{self.title} - {self.contact_number}"
