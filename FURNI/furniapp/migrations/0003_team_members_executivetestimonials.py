# Generated by Django 5.0.7 on 2024-07-19 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furniapp', '0002_team_members'),
    ]

    operations = [
        migrations.AddField(
            model_name='team_members',
            name='ExecutiveTestimonials',
            field=models.CharField(max_length=300, null=True),
        ),
    ]