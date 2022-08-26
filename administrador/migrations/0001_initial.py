# Generated by Django 4.1 on 2022-08-25 23:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Espacos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('descricao', models.TextField(max_length=1000)),
                ('imagem1', models.ImageField(blank=True, upload_to='fotos/espacos/imagem1')),
                ('imagem2', models.ImageField(blank=True, upload_to='fotos/espacos/imagem2')),
                ('imagem3', models.ImageField(blank=True, upload_to='fotos/espacos/imagem3')),
                ('imagem4', models.ImageField(blank=True, upload_to='fotos/espacos/imagem4')),
            ],
        ),
        migrations.CreateModel(
            name='NivelUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=3)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
