# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-23 12:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_key', models.CharField(db_index=True, max_length=40, verbose_name='Chave do Carrinho')),
                ('quantidade', models.PositiveIntegerField(default=1, verbose_name='Quantidade')),
                ('preco_p', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço')),
                ('total_p', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Total')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.Produto', verbose_name='Produto')),
            ],
            options={
                'verbose_name': 'Item do carrinho',
                'verbose_name_plural': 'Itens dos carrinhos',
            },
        ),
        migrations.CreateModel(
            name='ItemDoPedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField(default=1, verbose_name='Quantidade')),
                ('preco_p', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço')),
            ],
            options={
                'verbose_name': 'Item do pedido',
                'verbose_name_plural': 'Itens dos pedidos',
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(blank=True, choices=[(0, 'Aguardando pagamento'), (1, 'Concluída'), (2, 'Cancelada')], default=0, verbose_name='Situacao')),
                ('opcoes_de_pagamento', models.CharField(choices=[('deposito', 'Depósito'), ('pagseguro', 'PagSeguro'), ('paypal', 'PayPal')], default='deposito', max_length=20, verbose_name='Opcao de pagamento')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modificado', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
        ),
        migrations.AddField(
            model_name='itemdopedido',
            name='pedido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='checkout.Pedido', verbose_name='Pedido'),
        ),
        migrations.AddField(
            model_name='itemdopedido',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.Produto', verbose_name='Produto'),
        ),
        migrations.AlterUniqueTogether(
            name='cartitem',
            unique_together=set([('cart_key', 'produto')]),
        ),
    ]
