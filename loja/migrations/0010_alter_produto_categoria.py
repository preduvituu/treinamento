# Generated by Django 4.0.3 on 2022-04-07 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0009_alter_produto_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='loja.categoria'),
        ),
    ]