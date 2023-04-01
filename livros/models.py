from django.db import models
from uuid import uuid4

# Create your models here.

class livros(models.Model):
    id_livro = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    titulo = models.CharField(max_length=120)
    autor = models.CharField(max_length=120)
    ano_de_publicacao = models.CharField(max_length=120)
