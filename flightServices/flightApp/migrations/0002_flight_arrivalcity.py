# Generated by Django 3.2.9 on 2021-11-08 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='arrivalCity',
            field=models.CharField(default=None, max_length=20),
            preserve_default=False,
        ),
    ]