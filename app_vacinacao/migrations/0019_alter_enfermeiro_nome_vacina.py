# Generated by Django 3.2.8 on 2021-10-14 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_vacinacao', '0018_enfermeiro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enfermeiro',
            name='nome_vacina',
            field=models.CharField(max_length=50, verbose_name='Vacina'),
        ),
    ]
