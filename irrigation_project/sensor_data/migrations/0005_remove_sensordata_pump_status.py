# Generated by Django 5.1.2 on 2024-11-03 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sensor_data', '0004_irrigation_sensor_data_alter_irrigation_end_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensordata',
            name='pump_status',
        ),
    ]