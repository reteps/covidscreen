# Generated by Django 3.1.2 on 2020-11-23 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prescreen', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='custom_covid_screen',
        ),
        migrations.AlterField(
            model_name='account',
            name='events',
            field=models.ManyToManyField(blank=True, to='prescreen.Event'),
        ),
    ]
