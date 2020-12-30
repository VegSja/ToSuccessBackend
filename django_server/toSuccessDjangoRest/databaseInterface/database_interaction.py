from databaseInterface.models import Activity
from databaseInterface.serializers import ActivitySerializer

import calendar
import datetime
    
def retrieve_activities_from_db(user_request, daynumber, number_of_days):
    if daynumber == "" or number_of_days == "":
       activities = Activity.objects.filter(user=user_request)
    else:
       activities = Activity.objects.filter(user=user_request, date=daynumber)
       days_in_year = 365
       if calendar.isleap(datetime.datetime.now().year):
           days_in_year = 366
       for i in range(1, int(number_of_days)):
           daynumber_to_retrieve_from_db = str((int(daynumber)+i-1)%days_in_year+1)
           activities = activities | Activity.objects.filter(user=user_request, date=daynumber_to_retrieve_from_db)
    serializer = ActivitySerializer(activities, many=True)
    return serializer
