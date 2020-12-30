from databaseInterface.models import Activity
from databaseInterface.serializers import ActivitySerializer


    
def retrieve_activities_from_db(user_request, daynumber, number_of_days):
    if daynumber == "" or number_of_days == "":
       activities = Activity.objects.filter(user=user_request)
    else:
       activities = Activity.objects.filter(user=user_request, date=daynumber)
       for i in range(1, int(number_of_days)):
           daynumber_to_retrieve_from_db = str((int(daynumber)+i-1)%365+1)
           print(daynumber_to_retrieve_from_db)
           activities = activities | Activity.objects.filter(user=user_request, date=daynumber_to_retrieve_from_db)
    print("Activities: ", activities)
    serializer = ActivitySerializer(activities, many=True)
    return serializer
