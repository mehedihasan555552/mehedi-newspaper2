from django.contrib import admin
from . models import *
# Register your models here.

from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)



admin.site.register(LatestPost,PostAdmin)
admin.site.register(Post_of_the_day,PostAdmin)
admin.site.register(GasAndOil,PostAdmin)
admin.site.register(Criptocurrency,PostAdmin)
admin.site.register(Technology,PostAdmin)

admin.site.register(HeaderPost1,PostAdmin)
admin.site.register(HeaderPost2,PostAdmin)
