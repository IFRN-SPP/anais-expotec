# Generated by Django 5.0 on 2024-02-23 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_areas_artigos_normas_textos_delete_anal_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comissao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20, null=True)),
            ],
            options={
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Comissão',
            },
        ),
        migrations.CreateModel(
            name='Edicoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20, null=True)),
                ('imagem', models.ImageField(upload_to=None)),
            ],
            options={
                'verbose_name': 'Edição',
                'verbose_name_plural': 'Edições',
            },
        ),
    ]