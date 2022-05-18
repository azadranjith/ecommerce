# Generated by Django 4.0.4 on 2022-05-15 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cart_id',
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
