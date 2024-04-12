from app.models import Object
from rest_framework.serializers import ModelSerializer


class ObjectSerializer(ModelSerializer):
    class Meta:
        model = Object
        fields = "__all__"
