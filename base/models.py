from django.db import models
from django.utils import timezone
from embed_video.fields import EmbedVideoField
from multiselectfield import MultiSelectField


# Create your models here.


class LatestPost(models.Model):
    MY_CHOICES = ((1, 'Gas&Oil'),
              (2, 'Economy'),
              (3, 'Energy'),
              (5, 'Technology'))
    title = models.CharField(max_length=100)
    content = models.TextField()
    post_pic = models.ImageField(default='welcome.gif',null=True,blank=True)
    category = MultiSelectField(choices=MY_CHOICES,
                         max_choices=4,
                         max_length=30,null=True,blank=True)
    date_posted = models.DateTimeField(default=timezone.now)



    def __str__(self):
        return self.title







class MEOCHANNEL(models.Model):

    title = models.CharField(max_length=100)
    video = EmbedVideoField(blank=True)
    date_posted = models.DateTimeField(default=timezone.now)



    def __str__(self):
        return self.title
