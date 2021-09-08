from django.urls import path
from . import views
from django.urls.converters import register_converter
from .views import SearchResults

app_name = 'missing_persons'
urlpatterns = [
    path('home/', views.home, name='home'),
    #path('search_results/', SearchResults.as_view())
    path('search_results/', views.SearchResults)
    ]