# 
# apis/views.py
#from aching_wheels.cerebro_project.cerebro_project import missing_persons
#from aching_wheels.cerebro_project.cerebro_project import missing_persons
#from aching_wheels.cerebro_project.cerebro_project import missing_persons
#from aching_wheels.cerebro_project.cerebro_project import missing_persons
# from aching_wheels.cerebro_project.cerebro_project.missing_persons.models import Comment
from rest_framework.views import APIView
from rest_framework import viewsets, generics
from missing_persons import models
from .serializers import Missing_personSerializer, CommentSerializer
from rest_framework import filters
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response

# from aching_wheels.cerebro_project.cerebro_project.apis import serializers


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

class ListComment(generics.ListCreateAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = CommentSerializer

class DetailComment(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = CommentSerializer

class Missing_personComments(APIView):
    # def get_object(self, pk): 
    #     return models.Comment.objects.filter(missing_person=pk)

    def get(self, request, *args, **kwargs): 
        pk = self.kwargs["pk"]
        comments = models.Comment.objects.filter(missing_person=pk)
        serializer = CommentSerializer(comments, many=True)
        # response = serializer.data.__dict__
        return Response(serializer.data)
    def put(self, request, *args, **kwargs): 
        # pk = self.kwargs["pk"]
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    # def delete(self, request, *args, **kwargs):
    #     comment = models.Comment.get
    # serializer_class = CommentSerializer
    # def get_queryset(self): 
    #     missing_person = self.kwargs["pk"]
    #     queryset = models.Comment.objects.filter(missing_person=missing_person)


# class Comment(viewsets.ModelViewSet):
#     model = models.Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = (IsAuthenticated)
# @login_required
# def get_comments(request, pk):
#     queryset = models.Comment.objects.filter(pk=pk)
#     serializer = CommentSerializer(queryset, many=True)
#     return Response(serializer.data)