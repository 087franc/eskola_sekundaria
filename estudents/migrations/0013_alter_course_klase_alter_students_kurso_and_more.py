# Generated by Django 5.0.7 on 2024-11-07 12:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudents', '0012_alter_students_kurso_alter_students_materia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='klase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudents.klasse'),
        ),
        migrations.AlterField(
            model_name='students',
            name='kurso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudents.course'),
        ),
        migrations.AlterField(
            model_name='students',
            name='materia',
            field=models.ManyToManyField(related_name='students', to='estudents.subjects'),
        ),
    ]
