# Generated by Django 4.0.3 on 2022-04-07 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0010_alter_produto_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carro',
            name='produto',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='loja.produto'),
        ),
    ]