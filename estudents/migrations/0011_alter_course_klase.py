# Generated by Django 5.0.7 on 2024-11-07 12:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudents', '0010_alter_course_klase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='klase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='estudents.klasse'),
        ),
    ]
