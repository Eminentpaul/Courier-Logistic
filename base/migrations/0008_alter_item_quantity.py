# Generated by Django 4.2.3 on 2023-07-31 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_delivery_insurance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.IntegerField(default=1, null=True),
        ),
    ]
