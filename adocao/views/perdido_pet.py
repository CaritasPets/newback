from rest_framework.viewsets import ModelViewSet
from ..serializers import PetPerdidoSerializer
from ..models import PetPerdido

class PetPerdidoViewSet(ModelViewSet):
    queryset = PetPerdido.objects.all()
    serializer_class = PetPerdidoSerializer