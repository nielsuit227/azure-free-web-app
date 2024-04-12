from app.views import ListCreateObjects, RetrieveUpdateDestroyObjects
from django.urls import path

urlpatterns = [
    path("objects", ListCreateObjects.as_view()),
    path("objects/<int:pk>", RetrieveUpdateDestroyObjects.as_view()),
]
