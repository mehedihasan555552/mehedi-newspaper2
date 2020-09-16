from django.db import models
from django.utils import timezone
from embed_video.fields import EmbedVideoField
from multiselectfield import MultiSelectField


# Create your models here.


class LatestPost(models.Model):
    MY_CHOICES = ((1, 'Gas&Oil'),
              (2, 'Criptocurrency'),
              (3, 'Currency'),
              (4, 'Alternationveenergy'),
              (5, 'Technology'))
    title = models.CharField(max_length=100)
    content = models.TextField()
    post_pic = models.ImageField(default='welcome.gif',null=True,blank=True)
    category = MultiSelectField(choices=MY_CHOICES,
                         max_choices=5,
                         max_length=30,null=True,blank=True)
    date_posted = models.DateTimeField(default=timezone.now)



    def __str__(self):
        return self.title


class Post_of_the_day(models.Model):
    MY_CHOICES = ((1, 'Gas&Oil'),
              (2, 'Criptocurrency'),
              (3, 'Currency'),
              (4, 'Alternationveenergy'),
              (5, 'Technology'))
    title = models.CharField(max_length=100)
    content = models.TextField()
    post_pic = models.ImageField(default='welcome.gif',null=True,blank=True)
    category = MultiSelectField(choices=MY_CHOICES,
                         max_choices=5,
                         max_length=30,null=True,blank=True)
    date_posted = models.DateTimeField(default=timezone.now)



    def __str__(self):
        return self.title


class GasAndOil(models.Model):
    MY_CHOICES = ((1, 'Gas&Oil'),
              (2, 'Criptocurrency'),
              (3, 'Currency'),
              (4, 'Alternationveenergy'),
              (5, 'Technology'))
    title = models.CharField(max_length=100)
    content = models.TextField()
    post_pic = models.ImageField(default='welcome.gif',null=True,blank=True)
    category = MultiSelectField(choices=MY_CHOICES,
                         max_choices=5,
                         max_length=30,null=True,blank=True)
    date_posted = models.DateTimeField(default=timezone.now)



    def __str__(self):
        return self.title


class Criptocurrency(models.Model):
    MY_CHOICES = ((1, 'Gas&Oil'),
              (2, 'Criptocurrency'),
              (3, 'Currency'),
              (4, 'Alternationveenergy'),
              (5, 'Technology'))
    title = models.CharField(max_length=100)
    content = models.TextField()
    post_pic = models.ImageField(default='welcome.gif',null=True,blank=True)
    category = MultiSelectField(choices=MY_CHOICES,
                         max_choices=5,
                         max_length=30,null=True,blank=True)
    date_posted = models.DateTimeField(default=timezone.now)



    def __str__(self):
        return self.title


class Currency(models.Model):
    MY_CHOICES = ((1, 'Gas&Oil'),
              (2, 'Criptocurrency'),
              (3, 'Currency'),
              (4, 'Alternationveenergy'),
              (5, 'Technology'))
    title = models.CharField(max_length=100)
    content = models.TextField()
    post_pic = models.ImageField(default='welcome.gif',null=True,blank=True)
    category = MultiSelectField(choices=MY_CHOICES,
                         max_choices=5,
                         max_length=30,null=True,blank=True)
    date_posted = models.DateTimeField(default=timezone.now)



    def __str__(self):
        return self.title


class Technology(models.Model):
    MY_CHOICES = ((1, 'Gas&Oil'),
              (2, 'Criptocurrency'),
              (3, 'Currency'),
              (4, 'Alternationveenergy'),
              (5, 'Technology'))
    title = models.CharField(max_length=100)
    content = models.TextField()
    post_pic = models.ImageField(default='welcome.gif',null=True,blank=True)
    category = MultiSelectField(choices=MY_CHOICES,
                         max_choices=5,
                         max_length=30,null=True,blank=True)
    date_posted = models.DateTimeField(default=timezone.now)



    def __str__(self):
        return self.title


class HeaderPost1(models.Model):
    MY_CHOICES = ((1, 'Gas&Oil'),
              (2, 'Criptocurrency'),
              (3, 'Currency'),
              (4, 'Alternationveenergy'),
              (5, 'Technology'))
    title = models.CharField(max_length=100)
    content = models.TextField()
    post_pic = models.ImageField(default='welcome.gif',null=True,blank=True)
    category = MultiSelectField(choices=MY_CHOICES,
                         max_choices=5,
                         max_length=30,null=True,blank=True)
    date_posted = models.DateTimeField(default=timezone.now)



    def __str__(self):
        return self.title


class HeaderPost2(models.Model):
    MY_CHOICES = ((1, 'Gas&Oil'),
              (2, 'Criptocurrency'),
              (3, 'Currency'),
              (4, 'Alternationveenergy'),
              (5, 'Technology'))
    title = models.CharField(max_length=100)
    content = models.TextField()
    post_pic = models.ImageField(default='welcome.gif',null=True,blank=True)
    category = MultiSelectField(choices=MY_CHOICES,
                         max_choices=5,
                         max_length=30,null=True,blank=True)
    date_posted = models.DateTimeField(default=timezone.now)



    def __str__(self):
        return self.title


class MEOCHANNEL(models.Model):
    CATEGORY=(
        ('Gas&Oil', 'Gas&Oil'),
        ('Criptocurrency', 'Criptocurrency'),
        ('Currency', 'Currency'),
        ('Alternationveenergy', 'Alternationveenergy'),
        ('Technology', 'Technology'),

    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    video = EmbedVideoField(blank=True)
    category = models.CharField(max_length=200, choices=CATEGORY,blank=True)
    date_posted = models.DateTimeField(default=timezone.now)



    def __str__(self):
        return self.title
