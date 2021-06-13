# Generated by Django 3.2.3 on 2021-06-13 22:33

import core.models
from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20210613_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='novacolecaoindex',
            name='foto_index2',
            field=stdimage.models.StdImageField(default=2, upload_to=core.models.get_file_path, verbose_name='imagem'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='novacolecaoindex',
            name='preco2',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=109309130190, verbose_name='Preco'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='novacolecaoindex',
            name='titulo2',
            field=models.CharField(default=2, max_length=1000, verbose_name='Titulo'),
            preserve_default=False,
        ),
    ]