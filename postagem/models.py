from django.db import models
from django.core.validators import FileExtensionValidator
from core.models import Categoria


class Postagem(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(max_length=500)
    arquivo = models.FileField(upload_to='arquivos', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'ppt', 'pptx'])])
    data = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
