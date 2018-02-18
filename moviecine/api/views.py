from django.shortcuts import render
from rest_framework import viewsets

from main import models
from . import serializers

class FilmeViewSet(viewsets.ModelViewSet):
	queryset = models.Filme.objects.all()
	serializer_class = serializers.FilmeSerializer



class AtorViewSet(viewsets.ModelViewSet):
	queryset = models.Ator.objects.all()
	serializer_class = serializers.AtorSerializer




