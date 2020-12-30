from databaseInterface.models import Activity
from databaseInterface.serializers import ActivitySerializer
from databaseInterface.token_validation import token_validation
from .database_interaction import retrieve_activities_from_db

from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.utils import json

from django.contrib.auth.models import User
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests

from datetime import date
from datetime import datetime

class activity_list_view(APIView):
    permission_classes = (IsAuthenticated,)


    def get(self, request):
        user = request.user.username
        date_requested = request.GET.get('date', '')
        number_of_days_requested = request.GET.get('nb_days', '')
        print("Recived GET request", user, date_requested, number_of_days_requested)
        serializer = retrieve_activities_from_db(user, date_requested, number_of_days_requested)
        return JsonResponse(serializer.data, safe=False)
        
    def post(self, request):
        username = request.user.username
        data = JSONParser().parse(request)
        ##NOTE: THIS IS JUST FOR THE SAKE OF TRYING SOMETHING. SHOULD BE CHANGED
        data['user'] = username
        data_to_save = {}
        serializer = ActivitySerializer(data=data)
        print("Recived POST request", username)
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
            print("Checking if user exists....")
            user = User.objects.get(username=token.email)
        except User.DoesNotExist:
            print("Creating new user...")
            user = User()
            user.username = token.email
            # provider random default password
            user.password = make_password(BaseUserManager().make_random_password())
            user.email = token.email
            user.save()
            print("Successfully created new user...")

        #Genereate token without username and password
        token = RefreshToken.for_user(user)
        response = {}
        response['username'] = user.username
        response['access_token'] = str(token.access_token)
        response['refreash_token'] = str(token)
        return Response(response)

class activity_detail(APIView):
    permission_classes = (IsAuthenticated,)

    #This method is mainly used for deleting activities
    def delete(self, request, name):
        print("USER : " + request.user.username + " Sent a delete request")

        print("Trying to delete: " + request.user.username)
        try:
            activity = Activity.objects.get(activity_name=name, user=request.user.username)
        except Activity.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = ActivitySerializer(activity)
            return JsonResponse(serializer.data)

        if request.method == 'DELETE':
            activity.delete()
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)

class date_view(APIView):
    def get(self, request):
        response = {}
        response["date"] = date.today()
        response["daynumber"] = datetime.now().timetuple().tm_yday
        return Response(response)
