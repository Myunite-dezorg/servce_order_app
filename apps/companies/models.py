from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    is_airline = models.BooleanField(default=False)
    # tax_number = models.CharField(max_length=20)
    
    
    def __init__(self):
        return self.name
    
