from asyncio.windows_events import NULL
import json
from pickletools import read_uint1
from sched import scheduler
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser

from MedicarApp.models import Consult,Medic,ScheduleMedic
from MedicarApp.serializers import ConsultSerializer,MedicSerializer,ScheduleMedicSerializer
from datetime import datetime

# Create your views here.

@csrf_exempt
def MedicApi(request):
    if request.method == 'POST':
        data_medic = JSONParser().parse(request)
   
        serializers_medic = MedicSerializer(data=data_medic)
        verifcExistCrm = Medic.objects.filter(Crm = data_medic['Crm'])

        if len(verifcExistCrm) > 0:
            return JsonResponse("Medic already registered",safe=False)

        if serializers_medic.is_valid():
            serializers_medic.save()
            return JsonResponse(serializers_medic.data,safe=False,status= 201)
        return JsonResponse(serializers_medic.errors,safe=False,status= 401)

@csrf_exempt
def ScheduleMedicApi(request):
    if request.method == 'POST':
        data_schedule = JSONParser().parse(request)

        serializers_schedule = ScheduleMedicSerializer(data=data_schedule)
        date_shedule = datetime.fromisoformat(data_schedule['Day'])
        
        if date_shedule < datetime.fromisoformat(datetime.today().strftime('%Y-%m-%d')):
            return JsonResponse("Medic schedule has to be greater than the current day",safe=False,status = 401)

        verificExistMedic = Medic.objects.filter(MedicId = data_schedule['MedicId'])
        verificScheludeMedic = ScheduleMedic.objects.filter(MedicId = data_schedule['MedicId']).filter(Day = data_schedule['Day'])

        if len(verificExistMedic) == 0:
            return JsonResponse("Don't exit medic", safe=False,status=401)

        if len(verificScheludeMedic) > 0:
            return JsonResponse("Existing medic schedule",safe=False,status = 401)

        if serializers_schedule.is_valid():
            serializers_schedule.save()
            return JsonResponse(serializers_schedule.data,safe=False,status= 201)
        return JsonResponse(serializers_schedule.errors,safe=False,status= 401)
    elif request.method == 'GET':
        scheduler_ = ScheduleMedic.objects.all()
        scheduler_serealizer = ScheduleMedicSerializer(scheduler_,many=True)
        return JsonResponse(scheduler_serealizer.data,safe=False,status=200)


@csrf_exempt
def ConsultApi(request,id = 0):
    if request.method == 'POST':
        data_consult = JSONParser().parse(request)

        getSchedule = ScheduleMedic.objects.filter(ScheduleId = data_consult['ScheduleId']).first()
        
        if getSchedule == None:
            return JsonResponse("Unable to schedule consult",safe=False,status=401)

        if  getSchedule.Day < datetime.today().date():
            return JsonResponse("Unable to make consult", safe=False,status=401)

        hours = getSchedule.Hours.split(';')

        verifc = True

        for item in hours:
            if item == data_consult['Hour']:
                verifc = True
                break
            else:
                verifc = False

        if verifc == False:
            return JsonResponse("There is no time to schedule", safe=False,status=401)
                
        verificExistConsult = Consult.objects.filter(ScheduleId = data_consult['ScheduleId'],).filter(Hour = data_consult['Hour'])

        if len(verificExistConsult) > 0:
            return JsonResponse("There is a query for that time and day", safe=False,status=401)

        medic = Medic.objects.filter(MedicId = getSchedule.MedicId).first()

        data_serealize = {
            'DayConsult': getSchedule.Day,
            'Hour': data_consult['Hour'],
            'ScheduleId': data_consult['ScheduleId'],
            'SchedulingDate': datetime.today()
        }

        serializers_consult = ConsultSerializer(data=data_serealize)

        if serializers_consult.is_valid():
            serializers_consult.save()

            data_serealize_new = {
                        'Consult': serializers_consult.data,                        
                        'Medic': {
                            'MedicId': medic.MedicId,
                            'MedicName': medic.MedicName,
                            'Crm': medic.Crm,
                            'Email': medic.Email
                        }
                    }

            return JsonResponse(data_serealize_new,safe=False,status=201)
        return JsonResponse(serializers_consult.errors,safe=False,status=401)
    elif request.method == 'DELETE':
        consult = Consult.objects.get(ConsultId = id)

        if consult == NULL:
            return JsonResponse("Don't exist consult!",safe=False,status=401)

        if consult.DayConsult <  datetime.today().date():
            return JsonResponse("Consult already carried out!",safe=False,status=401)

        consult.delete()
        return JsonResponse("Delete!",safe=False,status=200)
    elif request.method == 'GET':
         consult = Consult.objects.all().order_by('DayConsult','Hour')
         consult_serealizer = ConsultSerializer(consult,many=True)
         return JsonResponse(consult_serealizer.data,safe=False,status=200)





