from django.contrib import admin
from .models import CustomUser, Debtors

# Register your models here.

admin.site.register(Debtors)


class MemberAdmin(admin.ModelAdmin):
  list_display = ("id","username","first_name", "last_name","email","dob","user_type")
  
admin.site.register(CustomUser, MemberAdmin)