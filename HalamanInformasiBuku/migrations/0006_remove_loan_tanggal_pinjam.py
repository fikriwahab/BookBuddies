# Generated by Django 4.2.6 on 2023-10-28 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HalamanInformasiBuku', '0005_loan_tanggal_pinjam'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loan',
            name='tanggal_pinjam',
        ),
    ]
