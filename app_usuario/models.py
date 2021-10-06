from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    cpf = models.CharField(max_length=45)
    nascimento = models.DateField()
    senha = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.email}'

    class Meta:
        db_table = 'usuario'

