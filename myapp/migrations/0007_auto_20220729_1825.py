# Generated by Django 3.2.8 on 2022-07-29 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_hh'),
    ]

    operations = [
        migrations.DeleteModel(
            name='health',
        ),
        migrations.DeleteModel(
            name='HH',
        ),
    ]
