# apis/urls.py
from django.urls import path

from .views import Missing_personViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', Missing_personViewSet, basename='Missing_person')
urlpatterns = router.urls
