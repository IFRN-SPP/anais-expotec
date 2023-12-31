# Generated by Django 5.0 on 2023-12-23 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_htmltext_nome_alter_htmltext_subtítulo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=100)),
                ('Área', models.CharField(choices=[('LINGUAGENS, CÓDIGOS E SUAS TECNOLOGIAS', 'LINGUAGENS, CÓDIGOS E SUAS TECNOLOGIAS'), ('CIÊNCIAS HUMANAS, SOCIAIS APLICADAS E SUAS TECNOLOGIAS', 'CIÊNCIAS HUMANAS, SOCIAIS APLICADAS E SUAS TECNOLOGIAS'), ('CIÊNCIAS DA NATUREZA E SUAS TECNOLOGIAS', 'CIÊNCIAS DA NATUREZA E SUAS TECNOLOGIAS'), ('MEIO AMBIENTE E SUAS TECNOLOGIAS', 'MEIO AMBIENTE E SUAS TECNOLOGIAS'), ('EDIFICAÇÕES E SUAS TECNOLOGIAS', 'EDIFICAÇÕES E SUAS TECNOLOGIAS'), ('INFORMÁTICA PARA INTERNET E SUAS TECNOLOGIAS', 'INFORMÁTICA PARA INTERNET E SUAS TECNOLOGIAS'), ('MATEMÁTICA E SUAS TECNOLOGIAS', 'MATEMÁTICA E SUAS TECNOLOGIAS')], max_length=55)),
                ('Equipe', models.CharField(max_length=100)),
            ],
        ),
    ]
