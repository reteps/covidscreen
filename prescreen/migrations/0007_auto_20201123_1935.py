# Generated by Django 3.1.2 on 2020-11-23 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prescreen', '0006_event_custom_questions'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CovidScreenDetails',
            new_name='CovidScreenData',
        ),
        migrations.RenameModel(
            old_name='CovidScreenQuestionSet',
            new_name='QuestionSet',
        ),
        migrations.RenameModel(
            old_name='CovidScreenInstance',
            new_name='Response',
        ),
    ]
