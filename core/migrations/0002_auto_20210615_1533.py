# Generated by Django 3.2.3 on 2021-06-15 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='botasindex',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=1000, verbose_name='Preco'),
        ),
        migrations.AlterField(
            model_name='novacolecaoindex',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=1000, verbose_name='Preco'),
        ),
        migrations.AlterField(
            model_name='novacolecaoindex',
            name='preco2',
            field=models.DecimalField(decimal_places=2, max_digits=1000, verbose_name='Preco 2'),
        ),
        migrations.AlterField(
            model_name='produtosindexprimeiracoluna',
            name='nome_tenis',
            field=models.CharField(max_length=1000, verbose_name='Nome do Tenis'),
        ),
        migrations.AlterField(
            model_name='produtosindexprimeiracoluna',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=1000, verbose_name='Preco'),
        ),
    ]
