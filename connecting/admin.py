from django.contrib import admin
from connecting.models import *
# Register your models here.

class connectAdmin(admin.ModelAdmin):
    list_display = ('connectId','postId','userId','doc','exchangeFlag')
admin.site.register(connectDetails, connectAdmin)