from django.contrib import admin

from .models import Cardapio

@admin.register(Cardapio)
class CardapioAdmin(admin.ModelAdmin):
    list_display = ('nome','ingrediente','preco', 'ativo', 'modificado')
