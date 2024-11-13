# Generated by Django 5.0.7 on 2024-11-10 15:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudents', '0023_merge_20241111_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controlukursuklase',
            name='klase',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='estudents.klasse'),
        ),
        migrations.AlterField(
            model_name='controlukursuklase',
            name='kurso',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='estudents.course'),
        ),
        migrations.AlterField(
            model_name='students',
            name='klase',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='students', to='estudents.klasse'),
        ),
        migrations.AlterField(
            model_name='students',
            name='kurso',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='estudents.course'),
        ),
    ]
