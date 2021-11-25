from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from app_jogo.models import Produtora, Jogo
from app_jogo.serializer import ProdutoraSerializer, JogoSerializer


class ProdutoraViewSet(ModelViewSet):
	queryset = Produtora.objects.all()
	serializer_class = ProdutoraSerializer


class JogoViewSet(ModelViewSet):
	queryset = Jogo.objects.all()
	serializer_class = JogoSerializer
