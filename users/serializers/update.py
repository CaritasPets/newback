from rest_framework import serializers
from ..models import CommonUser, OrganizationUser, User

class BaseUserUpdateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required = False)

    class Meta:
        model = User
        fields = ["username", "email", "foto", "password"]

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance

class CommonUserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommonUser
        exclude = ["user"]

class OrganizationUserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationUser
        exclude = ["user"]