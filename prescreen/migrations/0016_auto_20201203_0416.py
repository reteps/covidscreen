# Generated by Django 3.1.2 on 2020-12-03 04:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prescreen', '0015_auto_20201203_0411'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customquestionresponse',
            old_name='response',
            new_name='answered_for',
        ),
    ]
