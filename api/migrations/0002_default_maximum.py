# Generated by Django 3.1.4 on 2021-02-14 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='default',
            name='maximum',
            field=models.FloatField(default=0),
        ),
    ]
