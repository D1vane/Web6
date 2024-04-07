from django import template
import air.views as views
from air.models import AirTags
from django.db.models import Count
register = template.Library()

@register.inclusion_tag('air/air_list_tags.html')
def show_air_tags():
    return {"air_tags" : AirTags.objects.annotate(total=Count("tags")).filter(total__gt=0)}