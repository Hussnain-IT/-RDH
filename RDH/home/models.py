from django.conf import settings
from django.db import models


# Create your models here.

class Property(models.Model):
    PROPERTY_TYPES = [
        ('5_MARLA', '5 Marla'),
        ('7_MARLA', '7 Marla'),
        ('10_MARLA', '10 Marla'),
        ('1_KANAL', '1 Kanal'),
    ]
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('sold', 'Sold'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='properties')
    title = models.CharField(max_length=200)  
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES, blank=True, null=True)  
    image = models.ImageField(upload_to='property_images/')
    beds = models.IntegerField(blank=True, null=True)
    baths = models.IntegerField(blank=True, null=True) 
    area = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=200)
    owner = models.CharField(max_length=100)  
    email = models.EmailField()  
    phone = models.CharField(max_length=20) 
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(blank=True, null=True)  
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.location}"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
        
class Agent(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    image = models.ImageField(upload_to='agents/')
    
    def __str__(self):
        return self.name