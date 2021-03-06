# Generated by Django 3.1.2 on 2020-12-03 03:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prescreen', '0011_auto_20201203_0340'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomResponse',
            new_name='CustomQuestionResponse',
        ),
        migrations.RemoveField(
            model_name='response',
            name='details',
        ),
        migrations.AddField(
            model_name='response',
            name='contact_with_covid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='response',
            name='temperature',
            field=models.DecimalField(decimal_places=2, default=98.6, max_digits=5),
        ),
        migrations.AlterField(
            model_name='customquestionresponse',
            name='data',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='prescreen.response'),
        ),
        migrations.DeleteModel(
            name='CovidScreenData',
        ),
    ]
