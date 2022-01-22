# Generated by Django 3.2.7 on 2021-09-16 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_addpatient_assigndoctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='patient_Discription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientName', models.CharField(max_length=70)),
                ('usedMedicine', models.CharField(max_length=100)),
                ('diseaseName', models.CharField(max_length=200)),
                ('medicineUses', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='addpatient',
            name='assignDoctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.doctor'),
        ),
    ]
