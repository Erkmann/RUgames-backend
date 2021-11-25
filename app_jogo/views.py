from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from app_jogo.models import Produtora
from app_jogo.serializer import ProdutoraSerializer


class ProdutoraViewSet(ModelViewSet):
	queryset = Produtora.objects.all()
	serializer_class = ProdutoraSerializer
