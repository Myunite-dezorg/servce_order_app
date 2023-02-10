from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
from birthday import BirthdayField, BirthdayManager
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    # manager = models.OneToOneField(Manager, related_name="manager_profile", on_delete=models.CASCADE, null=True)
    # accounter = models.OneToOneField(Accounting, related_name="accounter_profile", on_delete=models.CASCADE, null=True)
    # partner = models.OneToOneField(Partner, related_name="partner_profile", on_delete=models.CASCADE, null=True)
    first_name = models.CharField(_("First Name"), max_length=50, null=True, blank=True)
    second_name = models.CharField(_("Second Name"), max_length=50, null=True, blank=True)
    last_name = models.CharField(_("Last Name"), max_length=50, null=True, blank=True)
    position = models.CharField("Position", max_length=50, null=True, blank=True)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    shift_work = models.BooleanField(_("Shift sched?"), default=0)
    birthday = BirthdayField(null=True)
    objects = BirthdayManager()
    

    avatar = models.ImageField(upload_to='images/users', default="")



    def get_model_fields(agent):
        return agent._meta.get_field('agent_id')

    # def get_model_fields(organization):
    #     return organization._meta.get_fields('organization_name')


    @property
    def thumbnail_preview(self):
        if self.avatar:
            return mark_safe('<img src="{}" width="80" />'.format(self.avatar.url))
        return ""

    def __str__(self):
        return self.user.get_username()


    @property
    def full_name(self):
     return "%s %s %s" % (self.first_name, self.last_name, self.second_name) 