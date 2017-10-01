from django.contrib import admin
from django.db import models
from . models import post1

class post1Admin(admin.ModelAdmin):
	list_display=['First_Name','Middle_Name','Last_Name','image','content','email',]
	fieldsets = (
        (None, {
            'fields': ('First_Name', 'Middle_Name', 'Last_Name')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('image', 'content', 'email'),
        }),
    )
admin.site.register(post1,post1Admin)