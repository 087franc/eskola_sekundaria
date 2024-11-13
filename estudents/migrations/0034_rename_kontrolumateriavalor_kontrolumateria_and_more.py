# Generated by Django 5.0.7 on 2024-11-12 05:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudents', '0033_alter_kontrolumateriavalor_controlukursuklase'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='KontroluMateriaValor',
            new_name='KontroluMateria',
        ),
        migrations.CreateModel(
            name='KontrolaEstudanteMateria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estudante', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='estudents.students')),
                ('kontrolumateria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudents.kontrolumateria')),
            ],
        ),
    ]