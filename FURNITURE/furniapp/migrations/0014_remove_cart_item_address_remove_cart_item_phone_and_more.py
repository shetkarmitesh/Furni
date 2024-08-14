# Generated by Django 5.0.7 on 2024-08-14 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furniapp', '0013_contactus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart_item',
            name='address',
        ),
        migrations.RemoveField(
            model_name='cart_item',
            name='phone',
        ),
        migrations.AddField(
            model_name='order',
            name='ProductName',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.FloatField(default=0.0),
        ),
    ]
