from rest_framework import serializers
from main import models


class AtorSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Ator
		fields = '__all__'


class FilmeSerializer(serializers.ModelSerializer):

	atores = AtorSerializer(many=True)

	class Meta:
		model = models.Filme
		fields = '__all__'