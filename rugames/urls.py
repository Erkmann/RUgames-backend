from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from app_jogo.views import ProdutoraViewSet, JogoViewSet
from app_usuario.views import UsuarioViewSet

router = routers.DefaultRouter()

router.register(r'usuario', UsuarioViewSet)
router.register(r'produtora', ProdutoraViewSet)
router.register(r'jogo', JogoViewSet)

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include(router.urls))
]
