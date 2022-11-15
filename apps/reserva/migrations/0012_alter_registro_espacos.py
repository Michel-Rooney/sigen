# Generated by Django 4.1 on 2022-11-15 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0007_alter_nivelusuario_status'),
        ('reserva', '0011_alter_confirmacao_registro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='espacos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrador.espacos'),
        ),
    ]