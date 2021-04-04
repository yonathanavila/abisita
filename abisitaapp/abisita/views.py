from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class AbisitaTemplateView(TemplateView):
    template_name = 'abisita/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Documento Evaluación'
        context['title1'] = 'Documento Evaluación'
        context['idEvaluacion'] = self.kwargs.get('idevaluacion')
        return context
