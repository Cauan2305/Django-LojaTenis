# Generated by Django 3.2.3 on 2021-06-15 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_alter_botasindex_texto_promocao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novacolecaoindex',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=10900, verbose_name='Preco'),
        ),
        migrations.AlterField(
            model_name='novacolecaoindex',
            name='preco2',
            field=models.DecimalField(decimal_places=2, max_digits=109300, verbose_name='Preco 2'),
        ),
    ]