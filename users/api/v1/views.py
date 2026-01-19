from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from users.api.v1.serializers import UserRegisterSerializer, ProfileSerializer


class UserRegisterCreateAPIView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]


class UserLoginAPIView(TokenObtainPairView):
    permission_classes = [AllowAny]


class ProfileRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user.profile
