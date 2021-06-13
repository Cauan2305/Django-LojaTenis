# Generated by Django 3.2.3 on 2021-06-12 01:50

import core.models
from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_novosprodutosindex_produtosindexprimeiracoluna'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProdutosIndexSegundaColuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto_tenis', stdimage.models.StdImageField(upload_to=core.models.get_file_path, verbose_name='imagem')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=109309130190, verbose_name='Preco')),
                ('nome_tenis', models.CharField(max_length=1000, verbose_name='Nome do Tenis')),
            ],
        ),
    ]