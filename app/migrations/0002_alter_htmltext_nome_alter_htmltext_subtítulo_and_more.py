# Generated by Django 5.0 on 2023-12-22 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='htmltext',
            name='Nome',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='htmltext',
            name='Subtítulo',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='htmltext',
            name='Texto',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='htmltext',
            name='Título',
            field=models.CharField(max_length=20),
        ),
    ]
