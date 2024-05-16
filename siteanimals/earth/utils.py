from .models import Earth
class DataMixin:
    title_page = None
    extra_context = {}
    model = Earth
    def __init__(self):
        if self.title_page:
            self.extra_context['title'] = self.title_page
            self.extra_context['header'] = self.title_page
    def get_mixin_context(self,context,**kwargs):
        if self.title_page:
            self.extra_context['title'] = self.title_page
            self.extra_context['header'] = self.title_page
        context.update(kwargs)
        return context