# Generated by Django 2.1.5 on 2019-02-08 07:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0039_auto_20190208_0714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 8, 7, 18, 49, 121120, tzinfo=utc)),
        ),
    ]
