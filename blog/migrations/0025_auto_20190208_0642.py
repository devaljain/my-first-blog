# Generated by Django 2.1.5 on 2019-02-08 06:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_auto_20190208_0600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 8, 6, 42, 22, 249337, tzinfo=utc)),
        ),
    ]
