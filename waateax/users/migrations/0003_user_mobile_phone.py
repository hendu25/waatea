# Generated by Django 3.0.10 on 2020-09-10 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='mobile_phone',
            field=models.IntegerField(blank=True, null=True, verbose_name='Mobile phone number'),
        ),
    ]