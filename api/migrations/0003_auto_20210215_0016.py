# Generated by Django 3.1.4 on 2021-02-15 00:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_default_maximum'),
    ]

    operations = [
        migrations.RenameField(
            model_name='default',
            old_name='minimun',
            new_name='minimum',
        ),
    ]
