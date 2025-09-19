from rest_framework.serializers import ModelSerializer
from ..models import OrganizationUser, CommonUser, User

class CommonUserSerializer(ModelSerializer):
    class Meta: 
        model = CommonUser
        fields = "__all__"
        depth = 1

class OrganizationSerializer(ModelSerializer):
    class Meta: 
        model = OrganizationUser
        fields = "__all__"
        depth = 1

class ProfileSerializer(ModelSerializer):
    common_profile = CommonUserSerializer(read_only=True)
    organization_profile = OrganizationSerializer(read_only=True)

    class Meta: 
        model = User
        fields = ['id', 'username', 'email', 'tipo', 'foto', 'common_profile', 'organization_profile']