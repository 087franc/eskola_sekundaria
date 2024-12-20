# Generated by Django 5.0.7 on 2024-11-10 15:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudents', '0018_remove_students_klase'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='klase',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='students', to='estudents.klasse'),
        ),
        migrations.AlterField(
            model_name='controlukursuklase',
            name='kurso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='estudents.course'),
        ),
    ]
