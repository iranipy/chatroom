# Generated by Django 3.2 on 2021-05-19 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatroom', '0002_privateroom'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='privateroom',
            name='slug',
        ),
    ]
