# apis/serializers.py
# from cerebro_project import missing_persons
from rest_framework import serializers
from missing_persons import models

class Missing_personSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'First_Name',
            'Last_Name',
            'eyecolor',
            'haircolor',
            'height_ft',
            'height_in',
            'weight',
            'race',
            'description_of_disappearance',
            'last_seen_latitude',
            'last_seen_longitude',
            'photo',
            'unique_markings'
        )
        model = models.Missing_person
