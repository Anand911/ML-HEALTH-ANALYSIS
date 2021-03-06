# Generated by Django 3.1.3 on 2022-06-07 14:24

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('health', '0003_auto_20220607_1952'),
    ]

    operations = [
        migrations.CreateModel(
            name='symptoms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symptom_name', models.CharField(max_length=100)),
                ('symptom_desc', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usersymptoms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_up_id', models.CharField(max_length=20)),
                ('timestamp', models.TimeField(default=datetime.datetime.now)),
                ('my_symptoms', models.ManyToManyField(to='health.symptoms')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
