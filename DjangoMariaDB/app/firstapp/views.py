# Create your views here.
#IMPORT models
from .models import Movie,ApiUsers

#IMPORT LIBRARIRES/FUNCTIONS
from django.shortcuts import render , HttpResponse
from django.http import JsonResponse
import json
from firstapp.customClasses import *
#IMPORT DJANGO PASSWORD HASH GENERATOR AND COMPARE
from django.contrib.auth.hashers import make_password, check_password

#check_password(noHashPassword,HashedPassword) this funcion validate if the password match to the hash

#def vista(request):
#    return render(request,'clase.html')

def vista(request):
    
    #https://docs.djangoproject.com/en/3.0/ref/templates/language/#templates
    return render(request, 'clase.html', {'title': "Bumblebee" , 'movies': Movie.objects.all()})


def vista2(request):
    
    #https://docs.djangoproject.com/en/3.0/ref/templates/language/#templates
    return render(request, 'dos.html', {'title': "Bumblebee" , 'movies': Movie.objects.all()})  

def login(request):

    ApiKey = 'Hola "'
    ApiKey = ApiKey.replace('"', '')

    responseData = {}
    responseData['result'] = 'error'
    responseData['message'] = ApiKey
    return JsonResponse(responseData, status=400)

    #VALIDATE METHOD
    if request.method == 'POST':

        #DECLARE RESPONSE
        responseData = {}

        #CHECK JSON STRUCTURE


        #CHECK JSON CONTENT


        #CHECK IF USER EXITST


        #TAKE PASSWORD OF THE USER

        #CHECK IF PASSWORD IS CORRECT


        #CHECK IF USER HAS API-KEY
        #obj.api_key = newApiKey
        #obj.save()


        #RETURN RESPONSE

    else:
        responseData = {}
        responseData['result'] = 'error'
        responseData['message'] = 'Invalid Request'
        return JsonResponse(responseData, status=400)


def makepassword(request,password):
    hashPassword = make_password(password)
    response_data = {}
    response_data['password'] = hashPassword
    return JsonResponse(response_data, status=200)
