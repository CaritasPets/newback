from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class LoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["username"] = user.username
        return token
    
    def validate(self, attrs):
        data = super().validate(attrs)

        data["message"] = f"Bem vindo, {self.user.username}!"
        data["user_id"] = self.user.id
        data["username"] = self.user.username

        return data