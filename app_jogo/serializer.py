from rest_framework.serializers import ModelSerializer

from app_jogo.models import Produtora, Jogo
from app_usuario.serializer import UsuarioSerializer


class ProdutoraSerializer(ModelSerializer):
	class Meta:
		model = Produtora
		fields = '__all__'


class JogoSerializer(ModelSerializer):
	produtora = ProdutoraSerializer('produtora')
	criador = UsuarioSerializer('criador')

	class Meta:
		model = Jogo
		fields = '__all__'
