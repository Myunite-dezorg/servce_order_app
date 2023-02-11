from django.db import models
from django.contrib.auth.models import User
import uuid

class Order(models.Model):
    ORDER_TYPE_CHOICES = [
        ('loading', 'Loading'),
        ('offloading', 'Offloading'),
        ('transporting', 'Transporting'),
        ('complex', 'Complex')
    ]
    ORDER_STATUS_CHOICES = [
        ('new', 'New'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]
    PAYMENT_STATES = [
        ('draft', 'Draft'),
        ('invoice', 'Invoice'),
        ('paid', 'Paid')
	]
    order_number = models.CharField(max_length=7, unique=True, default=uuid.uuid4().hex[:7].upper(), editable=False)
    order_type = models.CharField(max_length=20, choices=ORDER_TYPE_CHOICES)
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='new')
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATES, default='draft')
    cancel_reason = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_updated = models.DateTimeField(auto_now=True, editable=False)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='orders_created', editable=False)
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='orders_modified', editable=False)

    # other common fields

    class Meta:
        abstract = True