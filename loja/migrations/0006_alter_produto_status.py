# Generated by Django 4.0.3 on 2022-04-07 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0005_alter_produto_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='status',
            field=models.CharField(default='disponívell', max_length=30),
        ),
    ]
