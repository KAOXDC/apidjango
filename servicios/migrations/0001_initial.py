# Generated by Django 5.0.6 on 2024-11-21 01:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Aprendiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('edad', models.PositiveIntegerField()),
                ('vivo', models.BooleanField(default=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='aprendiz')),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='servicios.ciudad')),
                ('rol', models.ManyToManyField(blank=True, null=True, to='servicios.rol')),
            ],
        ),
    ]
