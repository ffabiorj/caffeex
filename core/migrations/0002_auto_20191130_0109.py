# Generated by Django 2.2.7 on 2019-11-30 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name stock'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='origin_farm',
            field=models.CharField(max_length=100, verbose_name='Origin farm'),
        ),
    ]
