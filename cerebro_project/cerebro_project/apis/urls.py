# apis/urls.py
from django.urls import path

from .views import Missing_personViewSet, SearchResults, ListMissing_person, DetailMissing_person, ListComment, DetailComment, Missing_personComments
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path('', ListMissing_person.as_view()),
    path('<int:pk>/', DetailMissing_person.as_view()),
    # path('bulletin/comments/<int:pk>/', views.get_comments, name="comments")
    path('comment/', ListComment.as_view()),
    path('comment/<int:pk>/', DetailComment.as_view()),
    path("person/comment/<int:pk>/", Missing_personComments.as_view())
]

router = DefaultRouter()
router.register('', Missing_personViewSet, basename='Missing_person')
urlpatterns += router.urls
urlpatterns.append(path('search/custom/',SearchResults.as_view(), name='nameSearch'))
# urlpatterns.append(path("comments/", Comment.as_view()))


# http://127.0.0.1:8000/apis/v1/search/custom/?search= users concatenate their search onto this url