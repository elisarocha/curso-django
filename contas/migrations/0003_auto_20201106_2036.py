# Generated by Django 3.1.2 on 2020-11-06 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0002_transacao'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Transacao',
            new_name='Transação',
        ),
        migrations.RenameField(
            model_name='transação',
            old_name='descricao',
            new_name='descrição',
        ),
    ]
