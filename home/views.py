from django.views.generic import TemplateView

from .models import Prato

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['pratos'] = Prato.objects.all()# .order_by('?').all() -Usar caso queira embaralhar como os icones aparecer na tela
        return context
