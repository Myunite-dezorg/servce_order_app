from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

class Company(models.Model):

    def get_user_name(self):
        return f"{self.user.username}-{self.user.email}"
    
    class Meta:
        ordering = ["name"]
        verbose_name = _("Company")
        verbose_name_plural = "Company profiles"
   
    user = models.OneToOneField(User,  on_delete=models.CASCADE)
    # user = models.OneToOneField(User, on_delete=models.PROTECT)
    name = models.CharField(
        _("Name"), max_length=50, default="")
    email = models.EmailField(_("Email"), blank=True, null=True)
    website = models.URLField(_("Website"), blank=True, null=True)
    phone = models.CharField(_("Phone"), max_length=40, null=True, blank=True)
    mobile = models.CharField(_("Mobile"), max_length=40, null=True, blank=True)
    address = models.CharField(_("Address"), max_length=128, null=True, blank=True)
    ogrn_number = models.CharField(_("ОГРН"), max_length=13, null=True, blank=True)
    inn_number = models.CharField(_("ИНН"), max_length=10, null=True, blank=True)
    kpp_number = models.CharField(_("КПП"), max_length=9, null=True, blank=True)
    logo = models.ImageField(upload_to='images/companies/logos')

    created_at = models.DateTimeField(_("created at"), auto_now_add=True, editable=False)
    last_modified = models.DateTimeField(_("last modified"), auto_now=True, editable=False)

    

    @property
    def phones(self):
        return ", ".join(filter(None, (self.phone, self.mobile)))
    
    @property
    def logo_preview(self):
        if self.logo:
            return mark_safe('<img src="{}" width="70" />'.format(self.logo.url))
        return ""
    
    
    def __str__(self):
        return f"{self.name}"
    
    def save(self, *args, **kwargs):
        if not self.name:
            self.name = f"{self.user.username} company LTD"
        super().save(*args, **kwargs)
    
