from django.contrib import admin

from .models import Prato,Receita

@admin.register(Prato)
class PratoAdmin(admin.ModelAdmin):
    list_display = ('nome','ingrediente','preco', 'ativo', 'modificado', 'imagem')

@admin.register(Receita)
class PratoAdmin(admin.ModelAdmin):
    list_display = ('nome','ingrediente','preparo', 'ativo', 'modificado', 'imagem')

