# Generated by Django 5.0.6 on 2024-06-28 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statelist_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('website', models.URLField(max_length=250)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Edification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=250)),
                ('country', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=500)),
                ('image', models.CharField(max_length=250)),
                ('active', models.BooleanField(default=True)),
                ('create', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Property',
        ),
    ]
