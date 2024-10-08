# Generated by Django 5.0.6 on 2024-07-19 18:10

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statelist_app', '0003_edification_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edification',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='edificacionlist', to='statelist_app.company'),
        ),
        migrations.CreateModel(
            name='Comentary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calification', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('text', models.CharField(max_length=200, null=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('edification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='statelist_app.edification')),
            ],
        ),
    ]
