# Generated by Django 3.1.2 on 2021-07-14 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_person'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.AddField(
            model_name='room',
            name='release',
            field=models.BooleanField(default=True),
        ),
    ]
