from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from ..serializers import (
    CommonUserUpdateSerializer,
    OrganizationUserUpdateSerializer,
    BaseUserUpdateSerializer
)

class UpdateProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user

        user_serializer = BaseUserUpdateSerializer(user, data=request.data, partial=True)

        if not user_serializer.is_valid():
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        user_serializer.save()

        if user.tipo == "common":
            profile = user.common_profile
            serializer = CommonUserUpdateSerializer(profile, data=request.data, partial=True)

        elif user.tipo == "organization":
            profile = user.organization_profile
            serializer = OrganizationUserUpdateSerializer(profile, data=request.data, partial=True)

        else:
            return Response({
                "error": "O tipo de usuário não é válido!"
            }, status=status.HTTP_400_BAD_REQUEST)
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                "user": user_serializer.data,
                "profile": serializer.data
            }, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)