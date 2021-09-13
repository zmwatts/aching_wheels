from apis.serializers import Missing_personSerializer
from .models import Missing_person
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import filters, generics

# Create your views here.
@login_required
def home(request):
    return render(request, 'missing_persons/home.html')
    
@login_required
def index(request, pk):
    return render(request, 'missing_persons/index.html', {pk:pk})

@login_required
class SearchResults(generics.ListAPIView):
    queryset = Missing_person.objects.all()
    serializer_class = Missing_personSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['First_Name', 'Last_Name']
    # def results(self, request):
    #     if request.method == 'POST':
    #         search_criteria = request.POST['search_criteria']
    #         results = Missing_person.objects.filter(filter_backends = request.search_fields.pk, search_criteria=search_criteria)
    #         context = {'results':results}
    #     return render(request, 'search.html', context)