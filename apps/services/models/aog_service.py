from django.db import models
import logging
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.shortcuts import reverse
from hashlib import sha1
from .abstract_service_class import AbstractService
from apps.stuffs.models import Aog, DutyPerson


logger = logging.getLogger(__name__)



class AogService(AbstractService):
   
    customer = models.ForeignKey(User, verbose_name=_("Customer service"), on_delete=models.CASCADE)
    service_name = models.CharField(
        _("Service name"), max_length=50, blank=False, null=False)
    flight = models.CharField(_("Flight"), max_length=6, default="")
    description = models.TextField(null=True, blank=True)
    aog_item = models.ManyToManyField(Aog)
  
    responsibles_persons = models.ManyToManyField(DutyPerson)
    comment = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return "[%s] %s" % (self.service_name, self.flight)


    def get_absolute_url(self):
        return reverse("LoadService", kwargs={"pk": self.pk})


    def save(self, *args, **kwargs):
        user = None
        request = kwargs.pop('request', None)
        if request and request.user.is_authenticated:
            user = request.user
        if self.pk:
            self.modified_by = user
        else:
            self.created_by = user
        super().save(*args, **kwargs)

