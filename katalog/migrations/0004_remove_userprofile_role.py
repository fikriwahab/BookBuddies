# Generated by Django 4.2.6 on 2023-12-10 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0003_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='role',
        ),
    ]