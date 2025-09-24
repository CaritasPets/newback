from rest_framework import serializers
from ..models import PetPerdido

class PetPerdidoSerializer(serializers.ModelSerializer):
    isFavorito = serializers.SerializerMethodField()

    class Meta:
        model = PetPerdido
        fields = "__all__"
        depth = 1

    def get_isFavorito(self, obj):
        user = self.context.get("request").user
        if user.is_authenticated:
            return obj.favoritos.filter(id=user.id).exists()
        return False