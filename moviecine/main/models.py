# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models


class Ator(models.Model):
    nome = models.CharField(max_length=150, verbose_name='Nome')
    imagem = models.ImageField(upload_to='atores/imagens/', verbose_name='Imagem', default='atores/imagens/no_image.png')

    class Meta:
        verbose_name = "Ator"
        verbose_name_plural = "Atores"
    
    def __unicode__(self):
        return self.nome

    def get_filmes_relacionados(self):
        return Filme.objects.filter(
            atores=self
        )[:20]

    def get_absolute_url(self):
        return '/ator/%i/' % self.pk


class Filme(models.Model):
    titulo = models.CharField(max_length=150, verbose_name='Titulo')
    titulo_principal = models.CharField(max_length=150, verbose_name='Titulo')
    slug = models.SlugField(max_length=50, verbose_name='Slug')
    duracao = models.TimeField(verbose_name='Duração')
    sinopse = models.TextField(verbose_name='Sinopse')
    imagem = models.ImageField(upload_to='filmes/imagens/', verbose_name='Imagem', default='filmes/imagens/no_image.png')
    likes = models.IntegerField(verbose_name='Likes')
    publicado = models.BooleanField(verbose_name='Publicado?')
    atores = models.ManyToManyField(Ator, verbose_name='Atores')

    class Meta:
        verbose_name = "Filme"
        verbose_name_plural = "Filmes"

    def __unicode__(self):
        return self.titulo

    def get_filmes_relacionados(self):
        return Filme.objects.filter(
            atores=self.atores.all(),
        ).exclude(
            pk=self.pk
        )[:10]


