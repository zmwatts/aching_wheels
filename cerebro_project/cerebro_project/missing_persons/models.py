# missing_personss/models.py
from django.db import models
from django.db.models.enums import TextChoices
from django.contrib.auth.models import User
import django.utils.timezone 
from datetime import datetime

class Eyecolor(models.Model):
    colors = (("GREEN", "GREEN"), ("BLUE", "BLUE"),("BLACK", "BLACK"), ("BROWN", "BROWN"), ("HAZEL", "HAZEL"), ("OTHER", "OTHER" ))
    color = models.CharField(choices=colors, max_length=13)
    def  __str__(self):
        return self.color

class Race(models.Model):
    races = (("WHITE", "WHITE"), ("AMERICAN INDIAN OR ALASKA NATIVE", "AMERICAN INDIAN OR ALASKA NATIVE"),("BLACK", "BLACK"), ("ASIAN", "ASIAN"), ("OTHER PACIFIC ISLANDER", "OTHER PACIFIC ISLANDER"), ("MULTIRACIAL", "MULTIRACIAL" ), ("OTHER", "OTHER" ), ("NATIVE HAWAIIAN", "NATIVE HAWAIIAN"))
    race = models.CharField(choices=races, max_length=70)
    def  __str__(self):
        return self.race

class Missing_person(models.Model):
    First_Name = models.CharField(blank=False, max_length=200)
    Last_Name = models.CharField(blank=False, max_length=200)
    eyecolor = models.ForeignKey(Eyecolor,on_delete=models.CASCADE, blank=True, null=True)
    haircolor = (models.CharField(max_length=200,blank=False))
    age = models.CharField(max_length=200,blank=False)
    sex = models.CharField(blank=True, max_length=50)
    date_last_contact = models.DateField(blank=False)
    height_ft = models.SmallIntegerField(blank=False)
    height_in = models.SmallIntegerField(blank=False)
    weight = models.IntegerField(blank=False)
    race = models.ForeignKey(Race,on_delete=models.CASCADE, blank=True, null=True)
    description_of_disappearance = models.CharField(max_length=1000)
    last_seen_latitude = models.FloatField(blank=False)
    last_seen_longitude = models.FloatField(blank=False)
    unique_markings = models.CharField(null=True,max_length=300)
    photo = models.ImageField(upload_to='cars')
    def __str__(self):
        return (f'{self.First_Name} {self.Last_Name}')

class Comment(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    content = models.CharField(blank=False, max_length=200)
    date_published = models.DateTimeField(blank=False, default=django.utils.timezone.now)
    date_editted = models.DateTimeField(blank=django.utils.timezone.now, default=django.utils.timezone.now)
    missing_person = models.ForeignKey(Missing_person,on_delete=models.CASCADE, blank=True, null=True, related_name='comments')
    def __str__(self):
        return f'{self.username}, {self.missing_person}'
