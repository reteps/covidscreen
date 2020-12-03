# Generated by Django 3.1.2 on 2020-12-03 03:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prescreen', '0008_auto_20201203_0324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='covidscreendata',
            name='custom_responses',
        ),
        migrations.AddField(
            model_name='customquestion',
            name='covid_screen_data',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='prescreen.covidscreendata'),
        ),
    ]