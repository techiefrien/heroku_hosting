from django.contrib import admin
from .models import *

# Register your models here.


class bookadmin(admin.ModelAdmin):
    list_display=['bname' , 'disc' , 'author' , 'branch' , 'download_count' , 'uploaded_at']


class catagoryadmin(admin.ModelAdmin):
    list_display=['catagory_name']

admin.site.register(products, bookadmin)
admin.site.register(catagory , catagoryadmin)