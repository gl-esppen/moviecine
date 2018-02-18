# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from main.models import Ator, Filme


class FilmeListView(ListView):
    model = Filme
    context_object_name = 'filmes'
    template_name = 'filmes.html'

    def get_queryset(self):
        queryset = Filme.objects.filter(publicado=True).order_by('titulo')
        order = self.request.GET.get('order', None)
        if order == 'likes':
            queryset = queryset.order_by('-likes')
        return queryset


class FilmeDetailView(DetailView):
    model = Filme
    context_object_name = 'filme'
    template_name = 'filme.html'


class AtorDetailView(DetailView):
    model = Ator
    context_object_name = 'ator'
    template_name = 'ator.html'


def AdicionarLikeFilme(request, slug=False, pk=False):
    if slug:
        movie = get_object_or_404(Filme, slug=slug)

    if pk:
        movie = get_object_or_404(Filme, pk=pk)

    movie.likes += 1
    movie.save(update_fields=['likes'])
    return redirect(movie.get_absolute_url())
