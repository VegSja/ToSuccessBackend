from databaseInterface.models import Activity, Category, Stats
from databaseInterface.serializers import ActivitySerializer, CategorySerializer, StatsSerializer
from databaseInterface.token_validation import token_validation
from .database_interaction import retrieve_activities_from_db, retrieve_categories_from_db
from .manage_stats import main

from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.utils import json
from rest_framework import status

from django.contrib.auth.models import User
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests

from datetime import date
from datetime import datetime
import random

class activity_list_view(APIView):
    permission_classes = (IsAuthenticated,)


    def get(self, request):
        user = request.user.username
        date_requested = request.GET.get('date', '')
        number_of_days_requested = request.GET.get('nb_days', '')
        serializer = retrieve_activities_from_db(user, date_requested, number_of_days_requested)
        return JsonResponse(serializer.data, safe=False)
        
    def post(self, request):
        username = request.user.username
        data = JSONParser().parse(request)
        ##NOTE: THIS IS JUST FOR THE SAKE OF TRYING SOMETHING. SHOULD BE CHANGED
        data['user'] = username
        data['unique_id'] = random.randint(1, 2147483646)
        data_to_save = {}
        serializer = ActivitySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class GoogleView(APIView):
    def post(self, request):
        payload = request.data.get("token") # Make readable
        token = token_validation(payload)

        # Create a user if no exist
        try:
            #Check if user exists already
            user = User.objects.get(username=token.email)
        except User.DoesNotExist:
            #Create new user
            user = User()
            user.username = token.email
            # provider random default password
            user.password = make_password(BaseUserManager().make_random_password())
            user.email = token.email
            user.save()

        #Genereate token without username and password
        token = RefreshToken.for_user(user)
        response = {}
        response['username'] = user.username
        response['access_token'] = str(token.access_token)
        response['refreash_token'] = str(token)
        print("User logged in: ", user.username)
        return Response(response)

class Logout(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            access_token = request.data["access_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response("Successfull logout", status=status.HTTP_205_RESET_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class activity_detail(APIView):
    permission_classes = (IsAuthenticated,)

    #This method is mainly used for deleting activities
    def delete(self, request, activity_id):
        try:
            activity = Activity.objects.get(unique_id=activity_id, user=request.user.username)
        except Activity.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = ActivitySerializer(activity)
            return JsonResponse(serializer.data)

        if request.method == 'DELETE':
            activity.delete()
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)

class category_view(APIView):
    permission_classes = (IsAuthenticated,)


    def get(self, request):
        user = request.user.username
        serializer = retrieve_categories_from_db(user)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        data = JSONParser().parse(request)
        username = request.user.username
        data["user"] = username
        data['unique_id'] = random.randint(1, 2147483646)
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class category_detail(APIView):
    permission_classes = (IsAuthenticated,)

    #This method is mainly used for deleting activities
    def delete(self, request, category_id):
        try:
            category = Category.objects.get(unique_id=category_id, user=request.user.username)
        except Activity.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = CategorySerializer(category)
            return JsonResponse(serializer.data)

        if request.method == 'DELETE':
            category.delete()
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)


class stats_view(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        main() #Just to test the writing and format of the data
        stats = stats.objects.all() #Change this further down the line
        serializer = StatsSerializer(stats)
        return JsonResponse(serializer.data)


class date_view(APIView):
    def get(self, request):
        response = {}
        response["date"] = date.today()
        response["daynumber"] = datetime.now().timetuple().tm_yday
        return Response(response)
