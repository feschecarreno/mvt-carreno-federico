# Generated by Django 4.1.2 on 2022-10-20 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desafio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='familiar',
            name='fecha_de_nacimiento',
            field=models.DateField(null=True),
        ),
    ]