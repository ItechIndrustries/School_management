# Generated by Django 2.2.7 on 2020-01-10 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20191209_2200'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='phone_no',
            field=models.BigIntegerField(default=1234567890),
        ),
    ]
