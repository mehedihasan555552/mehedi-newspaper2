# Generated by Django 3.0.6 on 2020-09-08 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20200906_1121'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='LatestPost',
        ),
    ]
