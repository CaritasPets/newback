from rest_framework.serializers import ModelSerializer
from ..models import PetPerdido

class PetPerdidoSerializer(ModelSerializer):
    class Meta:
        model = PetPerdido
        fields = "__all__"
        depth = 1