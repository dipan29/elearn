from django import template
from courses.models import Watched

register = template.Library()

@register.simple_tag
def has_watched(lesson, user):
    watched = Watched.objects.filter(lesson=lesson).filter(user=user)
    if(watched):
        return "✔️"
    else:
        return "👁️"