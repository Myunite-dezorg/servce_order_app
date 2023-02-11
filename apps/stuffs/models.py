from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from apps.stuffs.uuid import BaseUUID

# Create your models here.

class StoreLocation(BaseUUID):
    customer = models.ForeignKey(User, related_name='user_wrhs', on_delete=models.PROTECT)
    title = models.CharField(_("Store location name "), max_length=50)
    address = models.CharField(_("Address"), max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.title}"

    # def process_stock_fifo(aog, quantity):
    #     qty = quantity
    #     stocks = Aog.stock_set.all().order_by('timestamp')
    #     for stock in stocks:
    #         if qty > 0:
    #             qty_left = qty
    #             qty -= stock.quantity
    #         if qty >= 0:
    #             stock.delete()
    #         else: 
    #             stock.quantity = stock.quantity - qty_left stock.save()
    #         else:
    #             break

class BaseAgentStuff(BaseUUID):
    item = models.CharField(_("Item"), max_length=50, blank=True, null=True)
    # item_count = models.IntegerField(_("Count of item"))
    item_weight = models.CharField(_("Item weight"), max_length=50, blank=True, null=True)
    item_serial_number = models.CharField(
        _("Serial number"), max_length=20, blank=True, null=True)
    item_part_number = models.CharField(
        _("Part number"), max_length=20, blank=True, null=True)
    item_lenght = models.CharField(_("Item lenght"), max_length=50, blank=True, null=True)
    item_width = models.CharField(_("Item width"), max_length=50, blank=True, null=True)
    item_height = models.CharField(_("Item height"), max_length=50, blank=True, null=True)
    image_document = models.FileField(blank=True, null=True) 
    location_store = models.ForeignKey(StoreLocation, on_delete=models.PROTECT, null=True, blank=True)
    is_serviceable = models.BooleanField(default=True, verbose_name="Is Serviceable?")
    class Meta:
        abstract = True


class Aog(BaseAgentStuff):
    customer = models.ForeignKey(User, related_name='customer_aog', on_delete=models.PROTECT)
    image = models.ImageField(
        upload_to='images/stuffs/aogs', null=True, blank=True)

    def __str__(self):
        return self.item

    def image_tag(self):
        return u'<img src="%s" width="300"/>' % self.image.url  # Not bad code
    image_tag.allow_tags = True
    item_serial_number = None
    item_part_number = models.CharField(
        _("Part number"), max_length=20, blank=True, null=True)

    def __str__(self, *args):
        return f"{self.item} - {self.item_weight} | {self.item_part_number}"


class AcStand(BaseAgentStuff):
    customer = models.ForeignKey(User, related_name='customer_stand', on_delete=models.PROTECT)
    image = models.ImageField(
        upload_to='images/stuffs/stands', null=True, blank=True)

    def __str__(self):
        return self.item

    def image_tag(self):
        return u'<img src="%s" width="300"/>' % self.image.url  # Not bad code
    image_tag.allow_tags = True


class Instrument(BaseAgentStuff):
    customer = models.ForeignKey(User, related_name='customer_instrument', on_delete=models.PROTECT)
    image = models.ImageField(
        upload_to='images/stuffs/instr', null=True, blank=True)

    def __str__(self):
        return self.item

    def image_tag(self):
        return u'<img src="%s" width="300"/>' % self.image.url  # Not bad code
    image_tag.allow_tags = True


class AcEngine(BaseAgentStuff):
    customer = models.ForeignKey(User, related_name='customer_engine', on_delete=models.PROTECT)
    image = models.ImageField(
        upload_to='images/stuffs/engins', null=True, blank=True)

    def __str__(self):
        return f"{self.item} - {self.item_weight}"

    def image_tag(self):
        return u'<img src="%s" width="300"/>' % self.image.url  # Not bad code
    image_tag.allow_tags = True


class DutyPerson(BaseUUID):

    class Meta:
        verbose_name = _("Responsble person")
        verbose_name_plural = _("Responsibles")


    user = models.ForeignKey(User, verbose_name=_("Users persons stuff"), on_delete=models.CASCADE)
    full_name = models.CharField(_("Full Name"), max_length=50)
    position = models.CharField(_("Person position"), max_length=50)
    contact_phone = models.CharField(_("Contact Phone"), max_length=12)

    def __str__(self):
        return self.full_name