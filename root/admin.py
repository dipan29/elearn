from django.contrib import admin
from .models import Enroll, PageInfo, Testimonial
# Register your models here.
class EnrollAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'enable_access')
    list_filter = ('user', 'course', 'enable_access')


admin.site.register(Enroll, EnrollAdmin)
admin.site.register(PageInfo)
admin.site.register(Testimonial)