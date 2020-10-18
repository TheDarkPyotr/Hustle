from django.shortcuts import render
from django.db import models
from django.contrib.auth.decorators import login_required
from .models import Exam, Schedule
from django.db.models import Sum
import Esse3Api.api as esse3
import Esse3Api.endpoint
from getpass import getpass
from django.contrib.auth.models import User

  

@login_required
def dashboard(request):
    
    user = request.user
    username = user.profile.university_username
    password = user.profile.university_password
        
    api = esse3.Esse3API(Esse3Api.endpoint.endpoints['UNIPI']['url'], username, password)
    user_data = api.user()
    carriera = api.carriera()
    user_datalist = {'name' : user_data.name, 
                 'surname' : user_data.surname,
                 'cf': user_data.CF,
                 'group' : user_data.group,
                 'cds': carriera.corso_di_studi,
                 'matricola' : carriera.matricola,
                 'mat_id' : carriera.matId,
                 'university': user.profile.university
                  }
    
    libretto = api.libretto()

    exams = Exam.objects.all()
    schedule = Schedule.objects.all()
    cfu_sum = Exam.objects.filter(done=True).aggregate(Sum('cfu_number'))
    exam_stat = {'total' : Exam.objects.filter().count(),
                 'done' : Exam.objects.filter(done=False).count(),
                 'total_cfu' :  cfu_sum['cfu_number__sum'] }
    #schedule = Schedule.objects.raw("SELECT * FROM dashboard_schedule WHERE date = CURRENT_DATE")
    return render(request, 'dashboard.html', {'exams': exams, 'schedule': schedule, 'exam_stat': exam_stat, 'response': user_datalist, 'exam_list': libretto })

@login_required
def university(request):
    
    user = request.user
    username = user.profile.university_username
    password = user.profile.university_password
        
    api = esse3.Esse3API(Esse3Api.endpoint.endpoints['UNIPI']['url'], username, password)
    user_data = api.user()
    carriera = api.carriera()
    user_datalist = {'name' : user_data.name, 
                 'surname' : user_data.surname,
                 'cf': user_data.CF,
                 'group' : user_data.group,
                 'cds': carriera.corso_di_studi,
                 'matricola' : carriera.matricola,
                 'mat_id' : carriera.matId,
                 'university': user.profile.university
                  }
    
    libretto = api.libretto()

    exams = Exam.objects.all()
    schedule = Schedule.objects.all()
    cfu_sum = Exam.objects.filter(done=True).aggregate(Sum('cfu_number'))
    exam_stat = {'total' : Exam.objects.filter().count(),
                 'done' : Exam.objects.filter(done=False).count(),
                 'total_cfu' :  cfu_sum['cfu_number__sum'] }
    #schedule = Schedule.objects.raw("SELECT * FROM dashboard_schedule WHERE date = CURRENT_DATE")
    return render(request, 'university.html', {'exams': exams, 'schedule': schedule, 'exam_stat': exam_stat, 'response': user_datalist, 'exam_list': libretto })