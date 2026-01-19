from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from profiles.api.v1.serializers import ClientProfileSerializer, FreelancerProfileSerializer 


class ClientProfileCreateAPIView(generics.CreateAPIView):
    serializer_class = ClientProfileSerializer
    permission_classes = [IsAuthenticated]


class FreelancerProfileCreateAPIView(generics.CreateAPIView):
    serializer_class = FreelancerProfileSerializer
    permission_classes = [IsAuthenticated]
    