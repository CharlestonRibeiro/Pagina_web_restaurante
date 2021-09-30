from django.db import models

from stdimage.models import StdImageField
class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Cardapio(Base):
    nome = models.CharField('Nome', max_length=100)
    ingrediente = models.CharField('Ingrediente', max_length=500)
    preco =models.DecimalField('Preço', max_digits=5, decimal_places=2)
    imagem = StdImageField('Imagem', upload_to='pratos', validators={'thumb':{'width':700, 'height':700, 'crop': True}})

    class Meta:
        verbose_name = 'Cardapio'
        verbose_name_plural = 'Cardipios'

    def __str__(self):
        return self.nome

