# Generated by Django 4.2.7 on 2023-11-14 21:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auths', '0003_vacancy_publish_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curriculumvitae',
            name='birth_date',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 11, 15, 3, 26, 54, 603345), null=True, verbose_name='дата рождения'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='publish_date',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2023, 11, 15, 3, 26, 54, 603345), verbose_name='дата публикации'),
        ),
    ]
