# Generated by Django 3.1.2 on 2020-12-10 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prescreen', '0018_auto_20201210_0535'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.account'),
        ),
        migrations.AlterField(
            model_name='response',
            name='account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.account'),
        ),
        migrations.DeleteModel(
            name='Account',
        ),
    ]
