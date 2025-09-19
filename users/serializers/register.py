from rest_framework import serializers
from ..models import User, CommonUser, OrganizationUser

class RegisterSerializer(serializers.ModelSerializer):
    #normal
    nome = serializers.CharField(required=False)
    telefone = serializers.CharField(required=False)
    cpf = serializers.CharField(required=False)
    data_nascimento = serializers.DateField(required=False)

    #organization
    cnpj = serializers.CharField(required=False)
    instagram = serializers.CharField(required=False)
    facebook = serializers.CharField(required=False)
    endereco = serializers.CharField(required=False)
    descricao = serializers.CharField(required=False)


    class Meta:
        model = User
        fields = [
            'username', 'password', 'email', 'tipo', 'foto', 'nome', 'telefone', 'cpf', 'data_nascimento', 'cnpj', 'instagram', 'facebook', 'endereco', 'descricao'
        ]
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        tipo = validated_data.pop('tipo')

        common_data = {
            'nome': validated_data.pop('nome', None),
            'telefone': validated_data.pop('telefone', None),
            'cpf': validated_data.pop('cpf', None),
            'data_nascimento': validated_data.pop('data_nascimento', None),
        }

        org_data = {
            'cnpj': validated_data.pop('cnpj', None),
            'instagram': validated_data.pop('instagram', None),
            'facebook': validated_data.pop('facebook', None),
            'endereco': validated_data.pop('endereco', None),
            'descricao': validated_data.pop('descricao', None),
        }

        user = User(**validated_data, tipo=tipo)
        user.set_password(password)
        user.save()

        if tipo == 'common':
            CommonUser.objects.create(user=user, **common_data)
        elif tipo == 'organization':
            OrganizationUser.objects.create(user=user, **org_data)
        
        return user