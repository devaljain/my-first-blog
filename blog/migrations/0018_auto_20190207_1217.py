# Generated by Django 2.1.5 on 2019-02-07 12:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20190207_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 7, 12, 17, 45, 127001, tzinfo=utc)),
        ),
    ]
