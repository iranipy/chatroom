# Generated by Django 3.2 on 2021-05-19 12:02

import chatroom.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatroom', '0004_alter_privateroom_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privateroom',
            name='room_uid',
            field=models.CharField(default=chatroom.utils.uid_gen, editable=False, max_length=36, unique=True),
        ),
    ]