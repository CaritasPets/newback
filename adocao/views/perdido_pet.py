from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from ..serializers import PetPerdidoSerializer
from ..models import PetPerdido
from ..permissions import IsOwnerOrReadOnly

class PetPerdidoViewSet(ModelViewSet):
    queryset = PetPerdido.objects.all()
    serializer_class = PetPerdidoSerializer
    parser_classes = (MultiPartParser, FormParser)
    
    def get_permissions(self):
        if self.action == "create":
            permission_classes = [IsAuthenticated]
        elif self.action in ["update", "partial_update", "destroy"]:
            permission_classes = [IsOwnerOrReadOnly]
        else:
            permission_classes = []
        
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)