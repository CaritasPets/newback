from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser
from ..models import PetAdocao
from ..serializers import PetAdocaoSerializer
from ..permissions import IsOrganization, IsOwnerOrReadOnly

class PetAdocaoViewSet(ModelViewSet):
    queryset = PetAdocao.objects.all()
    serializer_class = PetAdocaoSerializer
    parser_classes = (MultiPartParser, FormParser)

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [IsOrganization]
        elif self.action in ["update", "partial_update", "destroy"]:
            permission_classes = [IsOwnerOrReadOnly]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
