from django.contrib import admin

from petstagram.common.models import PhotoComment


@admin.register(PhotoComment)
class PhotoComment(admin.ModelAdmin):
    pass