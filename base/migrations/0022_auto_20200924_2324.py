# Generated by Django 3.0.6 on 2020-09-24 17:24

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0021_auto_20200924_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='latestpost',
            name='category',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, 'Gas&Oil'), (2, 'Economy'), (3, 'Energy'), (5, 'Technology'), (4, 'Header')], max_length=30, null=True),
        ),
    ]
