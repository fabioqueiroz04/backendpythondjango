# Generated by Django 3.2.8 on 2021-10-10 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_vacinacao', '0006_vacina'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prioridades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idade', models.CharField(choices=[('Acima de 60 anos', 'Idosos'), ('Entre 30 e 59 anos', 'Adultos até 30 anos'), ('Entre 29 e 18 anor', 'Adultos abaixo de 30 anos'), ('Menores de 18 anos', 'Crianças e adolescentes')], max_length=30)),
            ],
        ),
    ]
