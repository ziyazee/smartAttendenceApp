from django.contrib import admin

# Register your models here.

from .models import Attendence
@admin.register(Attendence)
class  Ziya(admin.ModelAdmin):
    list_display=['usn','name','branch','year',]
