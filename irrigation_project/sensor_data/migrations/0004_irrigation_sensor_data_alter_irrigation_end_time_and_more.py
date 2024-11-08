# Generated by Django 5.1.2 on 2024-11-03 04:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensor_data', '0003_irrigation'),
    ]

    operations = [
        migrations.AddField(
            model_name='irrigation',
            name='sensor_data',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sensor_data.sensordata'),
        ),
        migrations.AlterField(
            model_name='irrigation',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='irrigation',
            name='water_used',
            field=models.FloatField(default=0.0),
        ),
    ]
