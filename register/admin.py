from django.contrib import admin
from register.models import users

# Register your models here.
class registerAdmin(admin.ModelAdmin):
    list_display = ('userId','name','email','contactNo','flags','location','dob','password')

admin.site.register(users,registerAdmin)