# -*- coding: utf-8 -*-

from django.contrib import admin
from main.models import Filme, Ator


class AtorAdmin(admin.ModelAdmin):
    list_display = ('nome',)

    search_fields = ['nome',]

    fieldsets = (
        ('Dados do Ator', {
            'fields': ('nome', 'imagem'),
        }),
    )


class FilmeAdmin(admin.ModelAdmin):

    list_display = ('titulo','titulo_principal','duracao', 'display_image', 'get_atores','publicado', 'likes')
    list_filter = ('atores__nome','publicado')

    search_fields = ['titulo','titulo_principal', 'atores__nome']

    fieldsets = (
        ('Dados do Filme', {
            'fields': ('titulo','titulo_principal','slug', 'duracao','likes', 'publicado','sinopse', 'imagem'),
        }),
        ('Atores', {
            'fields': ('atores',),
        }),
    )

    def display_image(self, obj):
        return '<img src="%s" width="200px"/>' % obj.imagem.url

    display_image.allow_tags = True

    def get_atores(self, obj):
        return "\n".join([a.nome for a in obj.atores.all()])



admin.site.register(Filme, FilmeAdmin)
admin.site.register(Ator, AtorAdmin)
