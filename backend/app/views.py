from app.models import Object
from app.serializers import ObjectSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class ListCreateObjects(ListCreateAPIView):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer


class RetrieveUpdateDestroyObjects(RetrieveUpdateDestroyAPIView):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer
