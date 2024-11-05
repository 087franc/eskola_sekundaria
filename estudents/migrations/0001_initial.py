# Generated by Django 5.0.7 on 2024-11-04 06:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Klasse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naran_klase', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Kurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naran_kursos', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naran', models.CharField(max_length=255)),
                ('sexo', models.CharField(choices=[('Hili Sexo', 'Hili Sexo'), ('Mane', 'Mane'), ('Feto', 'Feto'), ('Seluk', 'Seluk')], default='Hili Sexo', max_length=20)),
                ('no_telefone', models.CharField(max_length=15, null=True, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('hela_fatin', models.CharField(max_length=255)),
                ('municipio', models.CharField(choices=[('Hili Municipio', 'Hili Municipio'), ('Ainaro', 'Ainaro'), ('Aileu', 'Aileu'), ('Atauro', 'Atauro'), ('Bobonaro', 'Bobonaro'), ('Baucau', 'Baucau'), ('Dili', 'Dili'), ('Cova-Lima', 'Cova-Lima'), ('Ermera', 'Ermera'), ('Liquica', 'Liquica'), ('Lospalos', 'Lospalos'), ('Manatuto', 'Manatuto'), ('Manu-Fahi', 'Manu-Fahi'), ('Oecusse', 'Oecusse'), ('Viqueque', 'Viqueque')], default='Hili Municipio', max_length=20)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='professor')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naran_materia', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudents.kurso')),
                ('klase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudents.klasse')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudents.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Estudents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naran', models.CharField(max_length=255)),
                ('sexo', models.CharField(choices=[('Hili Sexo', 'Hili Sexo'), ('Mane', 'Mane'), ('Feto', 'Feto'), ('Seluk', 'Seluk')], default='Hili Sexo', max_length=20)),
                ('no_telefone', models.CharField(max_length=15, null=True, unique=True)),
                ('hela_fatin', models.CharField(max_length=255)),
                ('data_moris', models.DateField(null=True)),
                ('municipio', models.CharField(choices=[('Hili Municipio', 'Hili Municipio'), ('Ainaro', 'Ainaro'), ('Aileu', 'Aileu'), ('Atauro', 'Atauro'), ('Bobonaro', 'Bobonaro'), ('Baucau', 'Baucau'), ('Dili', 'Dili'), ('Cova-Lima', 'Cova-Lima'), ('Ermera', 'Ermera'), ('Liquica', 'Liquica'), ('Lospalos', 'Lospalos'), ('Manatuto', 'Manatuto'), ('Manu-Fahi', 'Manu-Fahi'), ('Viqueque', 'Viqueque')], default='Hili Municipio', max_length=20)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='estudante')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('klase', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='estudents.klasse')),
                ('materia', models.ManyToManyField(to='estudents.subjects')),
            ],
        ),
    ]