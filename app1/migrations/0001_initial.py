# Generated by Django 5.0.6 on 2024-12-09 17:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('sub', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('fee', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=100)),
                ('num', models.IntegerField()),
                ('paid', models.IntegerField()),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('sub', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.department')),
            ],
        ),
        migrations.CreateModel(
            name='Declaration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('verify', models.CharField(max_length=100)),
                ('sname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.student')),
            ],
        ),
    ]
