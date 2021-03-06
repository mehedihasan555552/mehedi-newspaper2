# Generated by Django 3.0.6 on 2020-08-18 17:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0002_post_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='TVPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('post_pic', models.ImageField(blank=True, default='welcome.gif', null=True, upload_to='')),
                ('category', models.CharField(blank=True, choices=[('Tarvel', 'Tarvel'), ('People', 'People'), ('Sports', 'Sports'), ('Music', 'Music'), ('Tv', 'Tv'), ('Entertainment', 'Entertainment')], max_length=200)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TravelPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('post_pic', models.ImageField(blank=True, default='welcome.gif', null=True, upload_to='')),
                ('category', models.CharField(blank=True, choices=[('Tarvel', 'Tarvel'), ('People', 'People'), ('Sports', 'Sports'), ('Music', 'Music'), ('Tv', 'Tv'), ('Entertainment', 'Entertainment')], max_length=200)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post_of_the_day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('post_pic', models.ImageField(blank=True, default='welcome.gif', null=True, upload_to='')),
                ('category', models.CharField(blank=True, choices=[('Tarvel', 'Tarvel'), ('People', 'People'), ('Sports', 'Sports'), ('Music', 'Music'), ('Tv', 'Tv'), ('Entertainment', 'Entertainment')], max_length=200)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MusicPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('post_pic', models.ImageField(blank=True, default='welcome.gif', null=True, upload_to='')),
                ('category', models.CharField(blank=True, choices=[('Tarvel', 'Tarvel'), ('People', 'People'), ('Sports', 'Sports'), ('Music', 'Music'), ('Tv', 'Tv'), ('Entertainment', 'Entertainment')], max_length=200)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
