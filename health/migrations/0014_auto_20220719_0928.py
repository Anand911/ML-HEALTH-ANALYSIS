# Generated by Django 3.1.3 on 2022-07-19 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0013_auto_20220719_0323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicines',
            name='medicine_type',
            field=models.CharField(choices=[('PILLS', 'PILLS'), ('TABLET', 'TABLET'), ('SYRINGE', 'SYRINGE'), ('SYRUP', 'SYRUP')], default='PILLS', max_length=30),
        ),
    ]