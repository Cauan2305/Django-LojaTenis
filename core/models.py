from django.db import models
from django.db.models.fields import CharField
from stdimage.models import StdImageField
import uuid

def get_file_path(__instance,filename):
    ext=filename.split('.')[-1]
    filename=f'{uuid.uuid4()}.{ext}'
    return filename

class NovaColecaoIndex(models.Model):
    # texto_colecao=models.TextField('Texto',max_length=1000,editable=True)
    foto_index=StdImageField('imagem',upload_to=get_file_path,variations={'thumb':{'width' : 366,'height':236 ,'crop':True}})
    preco=models.DecimalField('Preco',decimal_places=2,max_digits=10900)
    titulo=models.CharField('Titulo',max_length=1000)
    titulo2=models.CharField('Titulo 2',max_length=1000)
    preco2=models.DecimalField('Preco 2',decimal_places=2,max_digits=109300)
    foto_index2=StdImageField('imagem 2',upload_to=get_file_path,variations={'thumb':{'width' : 366,'height':236 ,'crop':True}})

    


class BotasIndex (models.Model):
    foto_index=StdImageField('imagem',upload_to=get_file_path,variations={'thumb':{'width' : 279,'height':279 ,'crop':True}})
    preco=models.DecimalField('Preco',decimal_places=2,max_digits=10930000)
    titulo=models.CharField('Titulo',max_length=1000)
    texto_promocao=CharField('Texto',max_length=10220000)

class ProdutosIndexPrimeiraColuna(models.Model):
    # pre_titulo=models.CharField('Pre Titulo',max_length=1000)
    # pre_texto=models.TextField('Texto',max_length=1000)
    foto_tenis=StdImageField('imagem',upload_to=get_file_path,variations={'thumb':{'width' : 189,'height':183 ,'crop':True}})
    preco=models.DecimalField('Preco',decimal_places=2,max_digits=10930000000)
    nome_tenis=models.CharField('Nome do Tenis',max_length=1000)



