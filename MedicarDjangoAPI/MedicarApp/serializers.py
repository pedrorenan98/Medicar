from rest_framework import serializers,fields
from MedicarApp.models import Consult,Medic,ScheduleMedic


class ConsultSerializer(serializers.ModelSerializer):
    DayConsult = fields.DateField(input_formats=['%Y-%m-%d'])
    class Meta:
        model = Consult
        fields = ('ConsultId','DayConsult','Hour','SchedulingDate','ScheduleId')

class MedicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medic
        fields = ['MedicId','MedicName','Crm','Email']

class ScheduleMedicSerializer(serializers.ModelSerializer):
    Day = fields.DateField(input_formats=['%Y-%m-%d'])
    class Meta:
        model = ScheduleMedic
        fields = ['ScheduleId','MedicId','Day','Hours']











