# Generated by Django 3.2.3 on 2021-06-28 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20210606_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='date1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='date2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='date3',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='date4',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='dur1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='dur2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='year1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='year2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='year3',
            field=models.CharField(max_length=100, null=True),
        ),
    ]