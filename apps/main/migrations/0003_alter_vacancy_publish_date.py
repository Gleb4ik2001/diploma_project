# Generated by Django 4.2.7 on 2024-01-13 22:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_vacancy_publish_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='publish_date',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2024, 1, 14, 4, 14, 21, 457708), verbose_name='дата публикации'),
        ),
    ]
