# Generated by Django 3.0.6 on 2020-09-18 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_auto_20200918_0005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meochannel',
            name='category',
        ),
        migrations.RemoveField(
            model_name='meochannel',
            name='content',
        ),
    ]