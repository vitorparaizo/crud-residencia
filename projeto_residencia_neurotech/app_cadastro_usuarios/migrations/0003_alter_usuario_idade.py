# Generated by Django 5.2 on 2025-04-27 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cadastro_usuarios', '0002_rename_usuarios_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='idade',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
