# Generated by Django 3.2.8 on 2021-10-10 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_vacinacao', '0005_delete_vacinas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_vacinas', models.CharField(max_length=50)),
            ],
        ),
    ]