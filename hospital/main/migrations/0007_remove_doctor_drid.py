# Generated by Django 3.2.7 on 2021-09-17 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_doctor_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='DrId',
        ),
    ]