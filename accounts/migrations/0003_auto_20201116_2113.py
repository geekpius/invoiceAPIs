# Generated by Django 3.1.3 on 2020-11-16 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20201116_2106'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='phone',
            new_name='phone_number',
        ),
    ]
