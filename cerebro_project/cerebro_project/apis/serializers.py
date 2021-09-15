# apis/serializers.py
# from cerebro_project import missing_persons
from django.db.models.query import QuerySet
from missing_persons.models import Missing_person
from rest_framework import serializers
from missing_persons import models
from missing_persons.models import Race, Comment

class RaceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Race
        fields=(
            'id',
            'race'
        )    

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=(
            'username',
            'content',
            'missing_person',
        )
        # depth=1

class Missing_personSerializer(serializers.ModelSerializer):
    #race = serializers.SlugRelatedField(queryset=Race.objects.all,slug_field="id")
    # race = Race.objects.get(race=Missing_person.race)
    race = RaceSerializer()
    comments = serializers.SlugRelatedField(many=True, slug_field="content", read_only=True)
    class Meta:
        fields = (
            'id',
            'First_Name',
            'Last_Name',
            'eyecolor',
            'haircolor',
            'age',
            'sex',
            'date_last_contact',
            'height_ft',
            'height_in',
            'weight',
            'race',
            'description_of_disappearance',
            'last_seen_latitude',
            'last_seen_longitude',
            'photo',
            'unique_markings',
            'comments'
        )
        model = models.Missing_person
        depth=1
