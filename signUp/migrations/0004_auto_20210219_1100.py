# Generated by Django 3.1.6 on 2021-02-19 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signUp', '0003_auto_20210218_0144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user_name',
            field=models.CharField(max_length=100),
        ),
    ]
