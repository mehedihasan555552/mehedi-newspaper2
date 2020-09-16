# Generated by Django 3.0.6 on 2020-09-16 10:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_auto_20200916_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criptocurrency',
            name='date_posted',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='currency',
            name='date_posted',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='gasandoil',
            name='date_posted',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='headerpost1',
            name='date_posted',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='headerpost2',
            name='date_posted',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='latestpost',
            name='date_posted',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='meochannel',
            name='date_posted',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='post_of_the_day',
            name='date_posted',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='technology',
            name='date_posted',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
