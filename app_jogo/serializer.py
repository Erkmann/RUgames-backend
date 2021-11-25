from rest_framework.serializers import ModelSerializer

from app_jogo.models import Produtora


class ProdutoraSerializer(ModelSerializer):
	class Meta:
		model = Produtora
		fields = '__all__'
