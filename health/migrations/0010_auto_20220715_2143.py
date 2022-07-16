# Generated by Django 3.1.3 on 2022-07-15 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0009_auto_20220712_2129'),
    ]

    operations = [
        migrations.CreateModel(
            name='medicine_prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeslot', models.CharField(choices=[(1, 'BREAK FAST'), (2, 'LUNCH'), (3, 'DINNER')], default=1, max_length=20)),
                ('before_food', models.BooleanField(default=True)),
                ('send_on', models.DateTimeField()),
                ('message', models.TextField(default='Its Time to take your medicine', max_length=200)),
                ('intake_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.profile')),
            ],
        ),
        migrations.RemoveField(
            model_name='medicines',
            name='intake_user',
        ),
        migrations.AlterField(
            model_name='medicines',
            name='time_slot',
            field=models.CharField(choices=[(1, 'BREAK FAST'), (2, 'LUNCH'), (3, 'DINNER')], default=1, max_length=20),
        ),
        migrations.CreateModel(
            name='track_medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_date', models.DateField()),
                ('took_medicines', models.BooleanField(default=False)),
                ('reminder_sent', models.BooleanField(default=False)),
                ('prescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='track_medicine', to='health.medicine_prescription')),
            ],
        ),
        migrations.AddField(
            model_name='medicine_prescription',
            name='medicines',
            field=models.ManyToManyField(to='health.Medicines'),
        ),
    ]