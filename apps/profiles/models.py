from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.companies.models import Company
from django.contrib.auth.models import User






class Company(models.Model):
    name = models.CharField(max_length=100)
    

        
    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.OneToOneField(Company, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(_("Fisrt name"), max_length=50, null=True, blank=True)
    second_name = models.CharField(_("Second name"), max_length=50, null=True, blank=True)
    last_name = models.CharField(_("Last name"), max_length=50, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.company:
            company = Company.objects.create(name='User Company')
            self.company = company
        super().save(*args, **kwargs)
        
        
    def __init__(self):
        return self.user.username