# Generated by Django 3.2.8 on 2022-08-01 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20220729_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartdb',
            name='user',
            field=models.CharField(default='', max_length=255),
        ),
    ]