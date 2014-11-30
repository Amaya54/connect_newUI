from django.contrib import admin
from posting.models import postDetails
# Register your models here.

class postAdmin(admin.ModelAdmin):
    list_display = ('postId', 'userId', 'dop')

admin.site.register(postDetails,postAdmin)