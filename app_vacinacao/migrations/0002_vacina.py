# Generated by Django 3.2.8 on 2021-10-10 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_vacinacao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacina',
            fields=[
                ('paciente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app_vacinacao.paciente')),
            ],
        ),
    ]
