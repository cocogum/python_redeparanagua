# Generated by Django 5.0.6 on 2024-05-14 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redeadmin', '0003_delete_servicos_comerciais_delete_servicos_sociais_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicos',
            name='preco',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
