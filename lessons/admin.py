from django.contrib import admin

from .models import Lesson


class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'video', 'lecturer', 'description', 'created_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'lecturer')

admin.site.register(Lesson, LessonAdmin)
