# Generated by Django 5.0.7 on 2024-11-10 15:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudents', '0015_anolectivo_remove_course_klase_controlukursuklase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anolectivo',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='klasse',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='klase',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='students', to='estudents.klasse'),
        ),
        migrations.AlterField(
            model_name='students',
            name='materia',
            field=models.ManyToManyField(blank=True, related_name='subjects', to='estudents.subjects'),
        ),
        migrations.AlterField(
            model_name='students',
            name='municipio',
            field=models.CharField(choices=[('Hili Municipio!', 'Hili Municipio!'), ('Ainaro', 'Ainaro'), ('Aileu', 'Aileu'), ('Atauro', 'Atauro'), ('Bobonaro', 'Bobonaro'), ('Baucau', 'Baucau'), ('Dili', 'Dili'), ('Cova-Lima', 'Cova-Lima'), ('Ermera', 'Ermera'), ('Liquica', 'Liquica'), ('Lospalos', 'Lospalos'), ('Manatuto', 'Manatuto'), ('Manu-Fahi', 'Manu-Fahi'), ('Viqueque', 'Viqueque')], default='Hili Municipio!', max_length=20),
        ),
        migrations.AlterField(
            model_name='students',
            name='sexo',
            field=models.CharField(choices=[('Hili Sexo!', 'Hili Sexo!'), ('Mane', 'Mane'), ('Feto', 'Feto'), ('Seluk', 'Seluk')], default='Hili Sexo!', max_length=20),
        ),
        migrations.AlterField(
            model_name='subjects',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='KlaseEstudante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('ativu', 'ativu'), ('nao-ativu', 'nao-ativu')], default='ativu', max_length=20)),
                ('controluestudante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='controlu', to='estudents.controlukursuklase')),
                ('estudante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estudante', to='estudents.students')),
                ('tinan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudents.anolectivo')),
            ],
        ),
    ]
