# Generated by Django 3.2.4 on 2021-06-19 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='booking_id',
        ),
    ]
