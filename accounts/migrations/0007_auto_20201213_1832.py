# Generated by Django 3.1.3 on 2020-12-13 18:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20201213_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='expired_at',
            field=models.DateField(default=datetime.datetime(2020, 12, 20, 18, 32, 8, 334164)),
        ),
    ]