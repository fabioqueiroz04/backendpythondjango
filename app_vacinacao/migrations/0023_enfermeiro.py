# Generated by Django 3.2.8 on 2021-10-14 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_vacinacao', '0022_delete_enfermeiro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enfermeiro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_enfermeiro', models.CharField(max_length=50)),
                ('nome_vacina', models.CharField(max_length=50)),
            ],
        ),
    ]
