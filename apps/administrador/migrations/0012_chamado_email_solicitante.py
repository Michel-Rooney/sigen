# Generated by Django 4.1 on 2022-11-29 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0011_alter_chamado_data_conclusao'),
    ]

    operations = [
        migrations.AddField(
            model_name='chamado',
            name='email_solicitante',
            field=models.EmailField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
