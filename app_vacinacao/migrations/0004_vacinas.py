# Generated by Django 3.2.8 on 2021-10-10 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_vacinacao', '0003_delete_vacina'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacinas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_vacina', models.CharField(max_length=50)),
            ],
        ),
    ]
