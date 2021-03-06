# Generated by Django 3.1.2 on 2021-07-24 13:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0004_auto_20210715_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='groups',
            field=models.ManyToManyField(default=None, to='base.Group'),
        ),
        migrations.AlterField(
            model_name='room',
            name='users',
            field=models.ManyToManyField(default=None, to=settings.AUTH_USER_MODEL),
        ),
    ]
