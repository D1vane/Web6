from django import template
import earth.views as views
from earth.models import EarthTags
from django.db.models import Count
register = template.Library()

@register.inclusion_tag('earth/earth_list_tags.html')
def show_earth_tags():
    return {"earth_tags" : EarthTags.objects.annotate(total=Count("tags")).filter(total__gt=0)}