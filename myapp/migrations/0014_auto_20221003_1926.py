# Generated by Django 3.2.8 on 2022-10-03 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_alter_hdd_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hdd',
            name='size',
            field=models.CharField(choices=[('3.5吋', '3.5吋'), ('2.5吋', '2.5吋')], default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='ssd',
            name='size',
            field=models.CharField(choices=[('M.2', 'M.2'), ('2.5吋', '2.5吋')], default='', max_length=255),
        ),
    ]
