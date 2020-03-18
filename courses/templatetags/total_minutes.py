from django import template
from django.db.models import Sum, Avg, Max, Min, Count

register = template.Library()


@register.filter
def total_minutes(queryset):
    return int(queryset.aggregate(Sum('duration')).get('duration__sum'))

@register.filter
def total_time(queryset):
    mins = total_minutes(queryset)
    if mins//60:
        hours = mins//60
        mins = mins - hours*60
        return str(hours)+(" Hours & " if hours>1 else " Hour ")+str(mins)+(" Minutes" if mins>1 else "Minute")
    else:
        return str(mins)+(" Minutes" if mins>1 else "Minute")
    