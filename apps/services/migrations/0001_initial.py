# Generated by Django 4.1.6 on 2023-02-10 20:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LoadingService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(default='3255829', editable=False, max_length=7, unique=True)),
                ('order_type', models.CharField(choices=[('loading', 'Loading'), ('offloading', 'Offloading'), ('transporting', 'Transporting'), ('complex', 'Complex')], max_length=20)),
                ('status', models.CharField(choices=[('new', 'New'), ('confirmed', 'Confirmed'), ('completed', 'Completed'), ('canceled', 'Canceled')], default='new', max_length=20)),
                ('payment_status', models.CharField(choices=[('draft', 'Draft'), ('invoice', 'Invoice'), ('paid', 'Paid')], default='draft', max_length=20)),
                ('cancel_reason', models.TextField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('service_name', models.CharField(max_length=50, verbose_name='Service name')),
                ('flight', models.CharField(default='', max_length=6, verbose_name='Flight')),
                ('description', models.TextField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders_created', to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Customer service')),
                ('modified_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders_modified', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
