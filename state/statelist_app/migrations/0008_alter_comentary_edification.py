# Generated by Django 5.0.6 on 2024-09-10 06:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statelist_app', '0007_edification_avg_calification_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentary',
            name='edification',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentaries', to='statelist_app.edification'),
        ),
    ]
