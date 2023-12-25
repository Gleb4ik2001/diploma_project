# Generated by Django 4.2.7 on 2023-12-25 15:37

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_vacancy_publish_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryChoices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='категория')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
                'ordering': ('-id',),
            },
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='publish_date',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2023, 12, 25, 21, 37, 40, 246926), verbose_name='дата публикации'),
        ),
        migrations.AlterField(
            model_name='curriculumvitae',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.categorychoices', verbose_name='категория'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.categorychoices', verbose_name='категория'),
        ),
    ]