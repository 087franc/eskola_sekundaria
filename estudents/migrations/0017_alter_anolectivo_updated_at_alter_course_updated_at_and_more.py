# Generated by Django 5.0.7 on 2024-11-10 15:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudents', '0016_alter_anolectivo_updated_at_alter_course_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anolectivo',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='klaseestudante',
            name='controluestudante',
            field=models.ForeignKey(on_delete=models.Model, related_name='controlu', to='estudents.controlukursuklase'),
        ),
        migrations.AlterField(
            model_name='klasse',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='klase',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='students', to='estudents.klasse'),
        ),
        migrations.AlterField(
            model_name='students',
            name='materia',
            field=models.ManyToManyField(blank=True, null=True, related_name='students', to='estudents.subjects'),
        ),
        migrations.AlterField(
            model_name='students',
            name='municipio',
            field=models.CharField(choices=[('Hili Municipio!', 'Hili Municipio!'), ('Ainaro', 'Ainaro'), ('Aileu', 'Aileu'), ('Atauro', 'Atauro'), ('Bobonaro', 'Bobonaro'), ('Baucau', 'Baucau'), ('Dili', 'Dili'), ('Cova-Lima', 'Cova-Lima'), ('Ermera', 'Ermera'), ('Liquica', 'Liquica'), ('Lospalos', 'Lospalos'), ('Manatuto', 'Manatuto'), ('Manu-Fahi', 'Manu-Fahi'), ('Viqueque', 'Viqueque')], default='Choose Municipality', max_length=20),
        ),
        migrations.AlterField(
            model_name='students',
            name='sexo',
            field=models.CharField(choices=[('Hili Sexo!', 'Hili Sexo!'), ('Mane', 'Mane'), ('Feto', 'Feto'), ('Seluk', 'Seluk')], default='Choose Gender', max_length=20),
        ),
        migrations.AlterField(
            model_name='subjects',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]