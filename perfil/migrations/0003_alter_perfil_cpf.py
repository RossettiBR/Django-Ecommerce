# Generated by Django 4.0.6 on 2022-07-11 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0002_alter_perfil_cep_alter_perfil_endereço_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='cpf',
            field=models.CharField(max_length=11, verbose_name='CPF'),
        ),
    ]
