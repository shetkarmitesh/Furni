# Generated by Django 5.0.7 on 2024-08-19 12:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furniapp', '0005_remove_cart_item_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='date',
            field=models.DateField(default=datetime.datetime.today),
        ),
    ]