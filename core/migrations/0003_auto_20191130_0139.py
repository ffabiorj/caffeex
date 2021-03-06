# Generated by Django 2.2.7 on 2019-11-30 01:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_auto_20191130_0109'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stock',
            options={'ordering': ['name']},
        ),
        migrations.RemoveField(
            model_name='coffeebag',
            name='type_coffee',
        ),
        migrations.AddField(
            model_name='coffeebag',
            name='coffee_type',
            field=models.CharField(default=1, max_length=50, verbose_name='Coffee type'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stock',
            name='coffee_types',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.CoffeeBag'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stock',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
