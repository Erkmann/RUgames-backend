from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from app_usuario.models import Usuario
from app_usuario.serializer import UsuarioSerializer


class UsuarioViewSet(ModelViewSet):
	queryset = Usuario.objects.all()
	serializer_class = UsuarioSerializer
