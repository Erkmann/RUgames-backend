from rest_framework.serializers import ModelSerializer

from app_usuario.models import Usuario


class UsuarioSerializer(ModelSerializer):
	class Meta:
		model = Usuario
		fields = '__all__'
