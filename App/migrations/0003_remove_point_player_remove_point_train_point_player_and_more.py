# Generated by Django 4.1.1 on 2022-09-29 09:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App', '0002_remove_point_feature_point_feature'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='point',
            name='player',
        ),
        migrations.RemoveField(
            model_name='point',
            name='train',
        ),
        migrations.AddField(
            model_name='point',
            name='player',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='بازیکن'),
        ),
        migrations.AddField(
            model_name='point',
            name='train',
            field=models.ManyToManyField(to='App.train', verbose_name='تمرین'),
        ),
    ]
