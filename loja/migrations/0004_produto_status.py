# Generated by Django 4.0.3 on 2022-04-07 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0003_produto_categoria_carro'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
