# Generated by Django 4.0.3 on 2022-04-07 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0006_alter_produto_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='status',
        ),
    ]