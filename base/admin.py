from django.contrib import admin
from . models import *
# Register your models here.

from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)




admin.site.register(LatestPost,PostAdmin)

admin.site.register(MEOCHANNEL)

admin.site.site_title = "Middle East OIL"
admin.site.site_header = "Middle East OIL"
admin.site.index_title = "Middle East OIL"
