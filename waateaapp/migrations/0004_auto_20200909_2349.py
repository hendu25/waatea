# Generated by Django 3.0.10 on 2020-09-09 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waateaapp', '0003_auto_20200909_2337'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='gameday',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]