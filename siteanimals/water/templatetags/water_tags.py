from django import template
import water.views as views
from water.models import WaterTags
from django.db.models import Count
register = template.Library()

@register.inclusion_tag('water/water_list_tags.html')
def show_water_tags():
    return {"tags_water" : WaterTags.objects.annotate(total=Count("tags")).filter(total__gt=0)}