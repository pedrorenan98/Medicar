# Generated by Django 4.0.3 on 2022-04-03 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consult',
            fields=[
                ('ConsultId', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('DayConsult', models.DateField()),
                ('Hour', models.CharField(max_length=50)),
                ('SchedulingDate', models.DateTimeField()),
                ('ScheduleId', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Medic',
            fields=[
                ('MedicId', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('MedicName', models.CharField(max_length=200)),
                ('Crm', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleMedic',
            fields=[
                ('ScheduleId', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('MedicId', models.PositiveIntegerField()),
                ('Day', models.DateField()),
                ('Hours', models.CharField(max_length=2000)),
            ],
        ),
    ]
