# Generated by Django 3.1.3 on 2022-07-16 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0010_auto_20220715_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkup',
            name='checkup_details',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='checkup',
            name='checkup_type',
            field=models.CharField(choices=[('DIABETES', 'DIABETES'), ('HEART DISEASE', 'HEART DISEASE'), ('SYMPTOMS CHECK', 'SYMPTOMS CHECK')], max_length=20),
        ),
        migrations.AlterField(
            model_name='checkup',
            name='checkup_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checkups', to='health.profile'),
        ),
        migrations.AlterField(
            model_name='medicine_prescription',
            name='timeslot',
            field=models.CharField(choices=[('BREAK FAST', 1), ('LUNCH', 2), ('DINNER', 3)], default=1, max_length=20),
        ),
        migrations.AlterField(
            model_name='medicines',
            name='time_slot',
            field=models.CharField(choices=[('BREAK FAST', 1), ('LUNCH', 2), ('DINNER', 3)], max_length=20),
        ),
    ]