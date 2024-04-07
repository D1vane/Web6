from django import template
import underground.views as views
from underground.models import UndergroundTags
from django.db.models import Count
register = template.Library()

@register.inclusion_tag('underground/underground_list_tags.html')
def show_underground_tags():
    return {"underground_tags" : UndergroundTags.objects.annotate(total=Count("tags")).filter(total__gt=0)}