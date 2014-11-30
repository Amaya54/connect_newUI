from django.contrib import admin
from login.models import login
# Register your models here.
class loginAdmin(admin.ModelAdmin):
    list_display = ('contactNo','email','password')
admin.site.register(login,loginAdmin)