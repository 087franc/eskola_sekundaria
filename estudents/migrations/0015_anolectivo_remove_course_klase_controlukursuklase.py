# Generated by Django 5.0.7 on 2024-11-07 23:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudents', '0014_alter_students_materia'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnoLectivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tinan', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='klase',
        ),
        migrations.CreateModel(
            name='ControluKursuKlase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('klase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudents.klasse')),
                ('kurso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudents.course')),
                ('tinan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudents.anolectivo')),
            ],
        ),
    ]
