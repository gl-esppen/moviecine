# -*- coding: utf-8 -*-

from django.views.generic import ListView, DetailView
from main.models import Ator, Filme

class FilmeListView(ListView):
    model = Filme
    context_object_name = 'filmes'
    template_name = 'filmes.html'

    def get_queryset(self):
        queryset = Filme.objects.all()

        #ordenacao
        if 'ordem' in self.request.GET:
            flow = self.request.GET.get('ordem')
            order = 'titulo' if flow == 'DESC' else '-nome'
            queryset = queryset.order_by(order)

        return queryset


class FilmeDetailView(DetailView):
    model = Filme
    context_object_name = 'filme'
    template_name = 'filme.html'


class AtorDetailView(DetailView):
    model = Ator
    context_object_name = 'ator'
    template_name = 'ator.html'