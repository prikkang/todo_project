# Generated by Django 5.0.2 on 2024-02-13 04:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 13, 4, 34, 31, 434434, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
