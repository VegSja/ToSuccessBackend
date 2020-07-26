from databaseInterface.models import Activity
from rest_framework import serializers

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'activity_name', 'minutes_after_midnight_start', 'minutes_after_midnight_end', 'date', 'user']