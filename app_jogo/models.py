from django.db import models

from app_usuario.models import Usuario


class Produtora(models.Model):
    nome = models.CharField(max_length=45)
    sigla = models.CharField(max_length=10)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'produtora'


class Jogo(models.Model):
    nome = models.CharField(max_length=255)
    imagem = models.CharField(max_length=255)
    publicacao = models.DateField()
    criador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='criador')
    produtora = models.ManyToManyField(db_table='jogo_produtora', related_name='produtoras', to=Produtora)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'jogo'
