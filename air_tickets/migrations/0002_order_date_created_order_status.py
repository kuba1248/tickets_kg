# Generated by Django 4.1 on 2022-08-09 07:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('air_tickets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('confirmed', 'confirmed'), ('reserved', 'reserved'), ('denied', 'denied'), ('returned', 'returned')], default='reserved', max_length=20),
        ),
    ]