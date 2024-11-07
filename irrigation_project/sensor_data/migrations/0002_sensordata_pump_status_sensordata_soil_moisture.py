# Generated by Django 5.1.2 on 2024-10-27 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensor_data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensordata',
            name='pump_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sensordata',
            name='soil_moisture',
            field=models.FloatField(default=0.0),
        ),
    ]
