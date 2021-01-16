from .models import Stats, Activity, Category

import json

def main(connected_username):
    #Resets db. Should not be used in future deployment
    Stats.objects.all().delete()
    
    #Get querylist of categories
    categories = get_categories_based_on_username(connected_username)

    #Create an empty stats dict with categories as keys. See format below
    stats_dict = create_category_dict(categories)

    category_names = query_to_key_list(categories, "name")
    for category in category_names:
        activities_query_list = get_activities_with_category(connected_username, category)
        stats_dict[category]["total_time"] = calculate_total_time(activities_query_list)

   
    json_to_save = json.dumps(stats_dict)
    

    ##Saves data as Stats object to DB
    data = Stats(username=connected_username, data=json_to_save)
    data.save()

    return

def get_activities_with_category(username, category):
    return Activity.objects.filter(user=username, activity_category=category)

def get_categories_based_on_username(username):
    return Category.objects.filter(user=username)

def query_to_key_list(query_to_use, key):
    return query_to_use.values_list(key, flat=True)

def create_category_dict(categories):
    categories = query_to_key_list(categories, "name")
    category_dict = {}
    for category in categories:
        category_color = categories.filter(name=category).values_list("color", flat=True)[0]
        category_dict[category] = {
                    "date_data" : {},
                    "total_time" : 0,
                    "color" : category_color,
                }
    return category_dict

#Funtion which takes acitivty querysetsi(For activities with the same category) as input and calculate time used per activity
def calculate_total_time(activities_query):
    total_time = 0

    print("Activity_queries: ", activities_query)
    #Loop through every activity in query
    for activity_query in activities_query:
        
        print("Activity_query: ", activity_query)

        #Get start_time
        start_time = activity_query.minutes_after_midnight_start 
   
        #Get end_time
        end_time = activity_query.minutes_after_midnight_end
    
        print("Times:", start_time, end_time)

        #Calculate total time
        total_time += end_time-start_time
    
    return total_time
