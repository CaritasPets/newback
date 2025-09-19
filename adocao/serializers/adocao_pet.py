from rest_framework.serializers import ModelSerializer
from ..models import PetAdocao

class PetAdocaoSerializer(ModelSerializer):
    class Meta:
        model = PetAdocao
        fields = "__all__"
        depth = 1