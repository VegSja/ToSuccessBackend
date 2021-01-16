from databaseInterface.models import Activity, Category, Stats
from rest_framework import serializers

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['activity_name', 'activity_category', 'minutes_after_midnight_start', 'minutes_after_midnight_end', 'date', 'date_string', 'user', 'unique_id']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'color', 'user', 'unique_id']


class StatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stats
        fields = ['username', 'data']
