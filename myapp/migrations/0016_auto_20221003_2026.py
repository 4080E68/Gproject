# Generated by Django 3.2.8 on 2022-10-03 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_auto_20221003_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpu',
            name='thread',
            field=models.IntegerField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='mb',
            name='foot_position_MB',
            field=models.CharField(choices=[('1200腳位', '1200腳位'), ('1700腳位', '1700腳位'), ('am4腳位', 'am4腳位')], default='', max_length=255),
        ),
    ]
