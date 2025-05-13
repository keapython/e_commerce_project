from django.contrib import admin

from common.models import MediaFile


# Register your models here.
@admin.register(MediaFile)
class MediaFileAdmin(admin.ModelAdmin):
    list_display = ("id", "file")   