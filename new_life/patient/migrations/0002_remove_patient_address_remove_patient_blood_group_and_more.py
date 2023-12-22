# Generated by Django 4.1.3 on 2023-01-19 04:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("patient", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="patient",
            name="address",
        ),
        migrations.RemoveField(
            model_name="patient",
            name="blood_group",
        ),
        migrations.RemoveField(
            model_name="patient",
            name="date_of_birth",
        ),
        migrations.RemoveField(
            model_name="patient",
            name="eid",
        ),
        migrations.RemoveField(
            model_name="patient",
            name="email",
        ),
        migrations.RemoveField(
            model_name="patient",
            name="full_name",
        ),
        migrations.RemoveField(
            model_name="patient",
            name="gender",
        ),
        migrations.RemoveField(
            model_name="patient",
            name="phone_number",
        ),
        migrations.RemoveField(
            model_name="patient",
            name="profile_pic",
        ),
        migrations.RemoveField(
            model_name="patient",
            name="registration_date_time",
        ),
    ]