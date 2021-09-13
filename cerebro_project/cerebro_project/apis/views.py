# apis/views.py
from rest_framework import viewsets, generics
from missing_persons import models
from .serializers import Missing_personSerializer
from rest_framework import filters


class Missing_personViewSet(viewsets.ModelViewSet):
    queryset = models.Missing_person.objects.all()
    serializer_class = Missing_personSerializer

class ListMissing_person(generics.ListCreateAPIView):
    queryset = models.Missing_person.objects.all()
    serializer_class = Missing_personSerializer


class DetailMissing_person(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Missing_person.objects.all()
    serializer_class = Missing_personSerializer

class SearchResults(generics.ListAPIView):
    queryset = models.Missing_person.objects.all()
    serializer_class = Missing_personSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^First_Name', '^Last_Name']