# Generated by Django 5.0.7 on 2024-08-05 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furniapp', '0006_cart_item_productname_alter_cart_item_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart_item',
            name='total',
            field=models.FloatField(default=0.0),
        ),
    ]
