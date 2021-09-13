# apis/urls.py
from django.urls import path

from .views import Missing_personViewSet, SearchResults, ListMissing_person, DetailMissing_person
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', ListMissing_person.as_view()),
    path('<int:pk>/', DetailMissing_person.as_view()),
]

router = DefaultRouter()
router.register('', Missing_personViewSet, basename='Missing_person')
urlpatterns = router.urls
urlpatterns.append(path('search/custom/',SearchResults.as_view(), name='nameSearch'))

# http://127.0.0.1:8000/apis/v1/search/custom/?search= users concatenate their search onto this url