# Generated by Django 2.1.7 on 2019-04-03 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0003_auto_20190403_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(allow_unicode=True, default='This is a new project', max_length=300, unique=True, verbose_name='slug'),
        ),
    ]
