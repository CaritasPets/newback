from rest_framework.viewsets import ModelViewSet
from ..models import PetAdocao
from ..serializers import PetAdocaoSerializer

class PetAdocaoViewSet(ModelViewSet):
    queryset = PetAdocao.objects.all()
    serializer_class = PetAdocaoSerializer