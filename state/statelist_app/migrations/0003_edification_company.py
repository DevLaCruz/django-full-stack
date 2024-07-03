# Generated by Django 5.0.6 on 2024-06-28 20:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statelist_app', '0002_company_edification_delete_property'),
    ]

    operations = [
        migrations.AddField(
            model_name='edification',
            name='company',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='edificacion', to='statelist_app.company'),
            preserve_default=False,
        ),
    ]