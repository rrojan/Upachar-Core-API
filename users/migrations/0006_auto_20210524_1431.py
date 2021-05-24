# Generated by Django 3.2.3 on 2021-05-24 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210524_1428'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_doctor',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='is_patient',
        ),
        migrations.AddField(
            model_name='profile',
            name='user_type',
            field=models.CharField(choices=[('patient', 'Patient'), ('doctor', 'Doctor')], default='patient', max_length=7),
        ),
    ]
