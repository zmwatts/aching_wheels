# apis/views.py
from rest_framework import viewsets
from missing_persons import models
from .serializers import Missing_personSerializer

class Missing_personViewSet(viewsets.ModelViewSet):
    queryset = models.Missing_person.objects.all()
    serializer_class = Missing_personSerializer