# Generated by Django 3.1.6 on 2021-02-07 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoodApp', '0004_alert_hospital'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(default='location', max_length=250),
        ),
    ]
