from django import template
import home.views as views

register = template.Library()

@register.simple_tag()
def get_classes():
    return views.data_inf
@register.inclusion_tag('home/list_of_classes.html')
def show_classes():
    data = views.data_inf
    return {'data':data}