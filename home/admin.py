from django.contrib import admin

from .models import Prato

@admin.register(Prato)
class PratoAdmin(admin.ModelAdmin):
    list_display = ('nome','ingrediente','preco', 'ativo', 'modificado', 'imagem')

