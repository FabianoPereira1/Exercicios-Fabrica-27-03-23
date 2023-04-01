from django.shortcuts import render
from rest_framework import viewsets
from livros import serializers
from livros import models

class livrosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.LivrosSerializers
    queryset = models.livros.objects.all()