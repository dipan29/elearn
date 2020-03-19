from django.contrib import admin
from .models import Enroll, PageInfo, Testimonial, Discount
# Register your models here.
class EnrollAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'enable_access')
    list_filter = ('user', 'course', 'enable_access')

class DiscountAdmin(admin.ModelAdmin):
    list_display = ('code', 'value')

admin.site.register(Enroll, EnrollAdmin)
admin.site.register(PageInfo)
admin.site.register(Testimonial)
admin.site.register(Discount, DiscountAdmin)