# Generated by Django 3.2.9 on 2021-11-09 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightApp', '0003_alter_reservation_flight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='middleName',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
