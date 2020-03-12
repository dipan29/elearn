from django.contrib import admin

from .models import Category, Course, Lesson, Comment


class CourseAdmin(admin.ModelAdmin):
    exclude = ('slug',)


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('slug',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'course',)
    list_filter = ('author', 'course',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Lesson)

