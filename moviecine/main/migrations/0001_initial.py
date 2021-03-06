# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-18 20:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('imagem', models.ImageField(default='atores/imagens/no_image.png', upload_to='atores/imagens/', verbose_name='Imagem')),
            ],
            options={
                'verbose_name': 'Ator',
                'verbose_name_plural': 'Atores',
            },
        ),
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150, verbose_name='Titulo')),
                ('titulo_original', models.CharField(max_length=150, verbose_name='Titulo Original')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('duracao', models.PositiveIntegerField(verbose_name='Dura\xe7\xe3o do filme em segundos')),
                ('sinopse', models.TextField(verbose_name='Sinopse')),
                ('imagem', models.ImageField(default='filmes/imagens/no_image.png', upload_to='filmes/imagens/', verbose_name='Imagem')),
                ('likes', models.IntegerField(verbose_name='Likes')),
                ('publicado', models.BooleanField(verbose_name='Publicado?')),
                ('atores', models.ManyToManyField(to='main.Ator', verbose_name='Atores')),
            ],
            options={
                'verbose_name': 'Filme',
                'verbose_name_plural': 'Filmes',
            },
        ),
    ]
