from django.db import models

# Create your models here.

# Cadastramento do medico

class Medic(models.Model):
    MedicId = models.AutoField(primary_key=True, auto_created = True)
    MedicName = models.CharField(max_length = 200)
    Crm = models.CharField(max_length = 50)
    Email = models.CharField(max_length = 100,blank=True)


# Agenda informa os dia e horarios disponiveis do medico
# Agenda do Medica

class ScheduleMedic(models.Model):
    ScheduleId = models.AutoField(primary_key=True, auto_created = True)
    MedicId = models.PositiveIntegerField()
    Day = models.DateField(serialize=False)
    Hours = models.CharField(max_length = 2000) 


# Cadastramento de Consulta
# Consulta marcadas

class Consult(models.Model):
    ConsultId =  models.AutoField(primary_key=True, auto_created = True)
    DayConsult = models.DateField()
    Hour = models.CharField(max_length = 50)
    SchedulingDate = models.DateTimeField()
    ScheduleId = models.PositiveIntegerField()