# Generated by Django 5.0.7 on 2024-11-10 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudents', '0018_alter_students_materia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='materia',
            field=models.ManyToManyField(blank=True, related_name='subjects', to='estudents.subjects'),
        ),
    ]
