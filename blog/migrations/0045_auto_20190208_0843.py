# Generated by Django 2.1.5 on 2019-02-08 08:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0044_auto_20190208_0839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 8, 8, 43, 18, 988543, tzinfo=utc)),
        ),
    ]
