# Generated by Django 2.1.5 on 2019-02-07 07:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190207_0659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 7, 7, 10, 9, 171078, tzinfo=utc)),
        ),
    ]
