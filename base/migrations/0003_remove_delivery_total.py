# Generated by Django 4.2.3 on 2023-07-30 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_delivery_delivery_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delivery',
            name='total',
        ),
    ]