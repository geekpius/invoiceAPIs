# Generated by Django 3.1.3 on 2020-12-13 18:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20201213_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='expired_at',
            field=models.DateField(default=datetime.datetime(2020, 12, 20, 18, 28, 44, 392437)),
        ),
    ]
