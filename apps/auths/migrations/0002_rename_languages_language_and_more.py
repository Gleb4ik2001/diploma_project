# Generated by Django 4.2.7 on 2023-11-14 21:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auths', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Languages',
            new_name='Language',
        ),
        migrations.AlterField(
            model_name='curriculumvitae',
            name='birth_date',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 11, 15, 3, 11, 1, 41295), null=True, verbose_name='дата рождения'),
        ),
    ]
