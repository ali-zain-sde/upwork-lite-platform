from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from profiles.permissions import IsClient, IsFreelancer
from profiles.models import ClientProfile, FreelancerProfile
from profiles.api.v1.serializers import (
    ClientProfileSerializer,
    FreelancerProfileSerializer,
    ClientProfileDetailSerializer,
    FreelancerProfileDetailSerializer,
    )


class ClientProfileCreateAPIView(generics.CreateAPIView):
    serializer_class = ClientProfileSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ClientProfileRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClientProfileDetailSerializer
    permission_classes = [IsAuthenticated, IsClient]

    def get_object(self):
        return get_object_or_404(ClientProfile, user=self.request.user)
    

class FreelancerProfileCreateAPIView(generics.CreateAPIView):
    serializer_class = FreelancerProfileSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FreelancerProfileRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FreelancerProfileDetailSerializer
    permission_classes = [IsAuthenticated, IsFreelancer]
    
    def get_object(self):
        return get_object_or_404(FreelancerProfile, user=self.request.user)
