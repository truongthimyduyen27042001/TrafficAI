from calendar import month
from cmath import e
from dataclasses import dataclass
from time import time
from django.shortcuts import render
from numpy import arange
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from datetime import datetime
from django.db.models.functions import TruncMonth,TruncDay
from django.db.models import Count
from calendar import monthrange 
import pandas as pd
# Create your views here.
import pyrebase
# neu co 2 cam thi 1 video luu roi tra ve cho fe hien len hoac la ben AI lam luon roi tra ve cho fe.
# config = {
#     "apiKey": "AIzaSyDrNUGAjDKbMnki_ZOKVkx5tZchBuC0bto",
#     "authDomain": "vehicle-detect-tracking.firebaseapp.com",
#     "databaseURL": "https://vehicle-detect-tracking-default-rtdb.firebaseio.com",
#     "projectId": "vehicle-detect-tracking",
#     "storageBucket": "vehicle-detect-tracking.appspot.com",
#     "messagingSenderId": "100481967903",
#     "appId": "1:100481967903:web:a1e9d50275dc4e507bb22a",
#     "measurementId": "G-BZYN2YPNSK"
# }
config = {
    "apiKey": "AIzaSyDPmJ7q83NlOnZy-RQgx3rRLE64Q3I-S0g",
    "authDomain": "uploadcsv-c8bfd.firebaseapp.com",
    "databaseURL": "https://uploadcsv-c8bfd-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "uploadcsv-c8bfd",
    "storageBucket": "uploadcsv-c8bfd.appspot.com",
    "messagingSenderId": "939407755660",
    "appId": "1:939407755660:web:9014bdb0c480453032eea9",
    "measurementId": "G-C7WC170JGF"
}
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = pd.read_csv('vehicle/mainFileVehicleIDdownload.csv')

def getData():
    data = VehicleSpeed.objects.all()
    if(data.count()>=1):
        data.delete()
        pass
    for i in database.values:
        ob = VehicleSpeed(  date = convert_datetime(i[1]),
                            time = i[2],
                            camera = i[3],
                            speed=float(i[4]),
                            number_plate="",
                            vehicle_type=i[5])
        ob.save()
    
def convert_datetime(date):
    ar= date.split('/')
    arr = {
        'Jan':'01',
        'Feb':'02',
        'Mar':'03',
        'Apr':'04',
        'May':'05',
        'Jun':'06',
        'Jul':'07',
        'Aug':'08',
        'Sep':'09',
        'Oct':'10',
        'Nov':'11',
        'Dec':'12',
    }
    ar[1]=arr[ar[1]]
    return (str(ar[2])+"-"+str(ar[1])+"-"+str(ar[0]))


def cam(data,camera):
    try:
        pass
    except Exception:
        print("Loi o get camera ham camera trong file view")
    if(type(camera)==str and camera=="ALL"):
        return data
    if(type(camera)==str and camera!=""):
        data = data.filter(camera = camera)
        return data
    return data
def year(year,camera):
    getData()
    data = VehicleSpeed.objects.filter(date__year=year)
    data = cam(data,camera)
    month__count = data.annotate(month=TruncMonth('date')).values('month').annotate(count=Count('id')).values('month', 'count')
    month_number__count = {}
    for i in arange(1,13):
        month_number__count[f'{i}'] = 0
    for i in month__count:
        var = i['month'].month
        month_number__count[f'{var}'] = i['count']
    print(month_number__count)
    context = get_vehicle_type(data)
    context['chart'] = month_number__count
    context['chart_tilte'] = "Month"
    return context

def day_month_year(date,camera):
    getData()
    data = VehicleSpeed.objects.filter(date=date)
    data = cam(data,camera)
    context = get_vehicle_type(data)
    return context

def get_vehicle_type(data):
    truck = data.filter(vehicle_type='Truck')
    car = data.filter(vehicle_type='Car')
    bus = data.filter(vehicle_type='Bus')
    motorcycle = data.filter(vehicle_type='Motorcycle')
    context = {
        "truck" : truck.count(),
        "car" : car.count(),
        "motorcycle" : motorcycle.count(),
        "bus" : bus.count(),
    }
    return context

def month_year(month,year,camera):
    getData()
    print(year)
    data = VehicleSpeed.objects.filter(date__month=month,date__year=year)
    data = cam(data,camera)
    day__count = data.annotate(day=TruncDay('date')).values('day').annotate(count=Count('id')).values('day', 'count')
    day_number__count = {}
    for i in arange(1,(monthrange(int(year), int(month))[1])+1):
        day_number__count[f'{i}'] = 0
    # print(day__count)
    for i in day__count:
        var = i['day'].day
        day_number__count[f'{var}'] = i['count']
    # print(day_number__count)
    context = get_vehicle_type(data)
    context['chart'] = day_number__count
    context['chart_title'] = "Day"
    return context

class VehicleViewSet(APIView):
    def get(self,request):
        getData()
        data = VehicleSpeed.objects.values_list('camera')
        cam = []
        for i in data:
            if i[0] not in cam:
                cam.append(i[0])
        day = request.query_params.get('day')
        month= request.query_params.get('month')
        year_ = request.query_params.get('year')
        camera = request.query_params.get('camera')
        print(day,month,year_,camera)
        context = []
        if day != "" and month != "" and year_ != "":
            date = year_+'-'+month+'-'+day
            context = day_month_year(date,camera)
        if day == "" and month == "" and year_ != "":
            context = year(year_,camera)
        if day == "" and month != "" and year_ != "":
            context = month_year((month),(year_),camera)
        return Response(context, status=status.HTTP_201_CREATED)
    
    def post(self,request):
        pass

class CamViewSet(APIView):
    def get(self,request):
        getData()
        data = VehicleSpeed.objects.values_list('camera')
        cam = []
        for i in data:
            if i[0] not in cam:
                cam.append(i[0])
        context = {
            "cam":cam
        }
        return Response(context, status=status.HTTP_201_CREATED)

