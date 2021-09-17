from django.urls import path
from . import views
from django.urls.converters import register_converter
from .views import SearchResults

app_name = 'missing_persons'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('bulletin/<int:pk>', views.index, name='index'),
    # path('bulletin/comments/<int:pk>/', views.get_comments, name="comments")
    #path('search_results/', SearchResults.as_view())
    #path('search_results/', views.SearchResults)
    ]