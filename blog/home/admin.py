from django.contrib import admin
from .models import *

# Register your models here.
# it is used for create table in admin pannel
@admin.register(Contact)
class StudentAdmin(admin.ModelAdmin):
    list_display=('name', 'email', 'subject', 'message')
# admin.site.register(Contact)


# @admin.register(Feedback)
class StudentAdmin(admin.ModelAdmin):
    list_display=('name', 'post', 'comment', 'image')
admin.site.register(Feedback,StudentAdmin)

@admin.register(Informations)
class StudentAdmin(admin.ModelAdmin):
    list_display=('address1', 'address2', 'phone', 'time','email')
# admin.site.register(Informations)
