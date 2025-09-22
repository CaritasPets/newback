from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from ..permissions import ListOnly
from ..serializers import OrganizationSerializer, CommonUserSerializer
from ..models import CommonUser, OrganizationUser

class ListOrganizationViewSet(ModelViewSet):
    queryset = OrganizationUser.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [ListOnly]

class ListCommonUserViewSet(ModelViewSet):
    queryset = CommonUser.objects.all()
    serializer_class = CommonUserSerializer
    permission_classes = [ListOnly]