from django.contrib import admin
from .models import Enroll
# Register your models here.
class EnrollAdmin(admin.ModelAdmin):
    list_display = ('user', 'course',)
    list_filter = ('user', 'course',)


admin.site.register(Enroll, EnrollAdmin)