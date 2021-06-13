from django.contrib import admin
from .models import BotasIndex,NovaColecaoIndex,ProdutosIndexPrimeiraColuna

@admin.register(BotasIndex)
class BotasAdmin(admin.ModelAdmin):
    list_display=('titulo',)
    
@admin.register(NovaColecaoIndex)
class ColecaoAdmin(admin.ModelAdmin):
    list_display=('titulo',)    
    readonly_fields=['texto_colecao']       
@admin.register(ProdutosIndexPrimeiraColuna)
class ProdutoPrimeiraColunaAdmin(admin.ModelAdmin):
    list_display=('nome_tenis','preco',)

