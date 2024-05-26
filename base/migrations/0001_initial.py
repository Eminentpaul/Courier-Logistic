# Generated by Django 4.2.3 on 2023-07-30 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_name', models.CharField(max_length=200, null=True)),
                ('sender_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('sender_phone', models.CharField(max_length=20)),
                ('receivers_name', models.CharField(max_length=200, null=True)),
                ('receivers_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('receivers_phone', models.CharField(max_length=20)),
                ('receivers_address', models.CharField(blank=True, max_length=255, null=True)),
                ('delivery_status', models.CharField(choices=[('Not Yet Shipped', 'Not Yet Shipped'), ('Shipped', 'Shipped'), ('Cancelled', 'Cancelled'), ('Refunded', 'Refunded'), ('Pending', 'Pending')], default='Not Yet Shipped', max_length=120)),
                ('payment_status', models.CharField(choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')], default='Unpaid', max_length=120)),
                ('clearance_cost', models.DecimalField(decimal_places=2, default=0.0, max_digits=10000)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=100)),
                ('tracking_id', models.CharField(blank=True, max_length=9, null=True, unique=True)),
                ('created', models.DateField(auto_now=True)),
                ('updated', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('weight', models.DecimalField(decimal_places=2, default=1.0, max_digits=300)),
                ('quantity', models.FloatField(default=1.0)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
                ('shipping_cost', models.DecimalField(decimal_places=2, default=0.0, max_digits=10000)),
                ('receiver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.delivery')),
            ],
        ),
    ]