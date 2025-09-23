from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from ..models import PetAdocao, PetPerdido
from ..serializers import PetAdocaoSerializer, PetPerdidoSerializer

class FavoritoViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def toggle_adocao(self, request, pk=None):
        pet = get_object_or_404(PetAdocao, pk=pk)
        user = request.user

        if pet.favoritos.filter(id=user.id).exists():
            pet.favoritos.remove(user)
            return Response({
                "detail": "Removido dos Favoritos!"
            }, status=200)
        else:
            pet.favoritos.add(user)
            return Response({
                "detail": "Adicionado aos Favoritos!"
            }, status=201)
        
    def toggle_perdido(self, request, pk=None):
        pet = get_object_or_404(PetPerdido, pk=pk)
        user = request.user

        if pet.favoritos.filter(id=user.id).exists():
            pet.favoritos.remove(user)
            return Response({"detail": "Removido dos favoritos"}, status=200)
        else:
            pet.favoritos.add(user)
            return Response({"detail": "Adicionado aos favoritos"}, status=201)
        
    def list_adocao(self, request):
        user = request.user
        pets = PetAdocao.objects.filter(favoritos=user)
        serializer = PetAdocaoSerializer(pets, many=True, context={"request": request})
        return Response(serializer.data)

    def list_perdido(self, request):
        user = request.user
        pets = PetPerdido.objects.filter(favoritos=user)
        serializer = PetPerdidoSerializer(pets, many=True, context={"request": request})
        return Response(serializer.data)