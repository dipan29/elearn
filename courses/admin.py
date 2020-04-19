from django.contrib import admin

from .models import Category, Course, Lesson, Comment, Tag, Watched

class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course',)
    list_filter = ('course',)

class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course',)
    list_filter = ('course',)

class CourseAdmin(admin.ModelAdmin):
    exclude = ('slug',)


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('slug',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'course',)
    list_filter = ('author', 'course',)

class TagAdmin(admin.ModelAdmin):
    list_display = ('category', 'course',)
    list_filter = ('course', 'category')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Tag, TagAdmin)
# admin.site.register(Watched)

