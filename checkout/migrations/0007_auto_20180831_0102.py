# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-31 04:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_auto_20180831_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='opcoes_de_pagamento',
            field=models.CharField(choices=[('deposito', 'Depósito'), ('pagseguro', 'PagSeguro'), ('paypal', 'PayPal')], default='deposito', max_length=20, verbose_name='Opcao de pagamento'),
        ),
    ]