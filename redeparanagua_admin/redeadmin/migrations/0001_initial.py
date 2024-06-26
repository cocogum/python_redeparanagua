# Generated by Django 5.0.6 on 2024-05-13 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servicos_Comerciais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_solicitacao', models.IntegerField()),
                ('nome_servicoCom', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=1200)),
                ('quantidade', models.IntegerField()),
                ('Id_Individuo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Servicos_Sociais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_solicitacao', models.IntegerField()),
                ('nome_servicoCom', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=1200)),
                ('quantidade', models.IntegerField()),
                ('Id_Individuo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Servicos_tecnicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_solicitacao', models.IntegerField()),
                ('nome_servicoCom', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=1200)),
                ('quantidade', models.IntegerField()),
                ('Id_Individuo', models.IntegerField()),
            ],
        ),
    ]
