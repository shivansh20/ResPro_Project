# Generated by Django 3.2.3 on 2021-06-01 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20210601_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='projdur1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='projdur2',
            field=models.CharField(max_length=100, null=True),
        ),
    ]