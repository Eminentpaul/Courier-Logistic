# Generated by Django 4.2.3 on 2023-07-31 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_delivery_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='sender_address',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
