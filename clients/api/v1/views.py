from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from core.permissions import IsClient
from clients.models import ClientProfile, Project
from clients.api.v1.serializers import ProjectSerializer
from clients.api.v1.serializers import (
    ClientProfileSerializer,
    ClientProfileDetailSerializer,
    ProjectSerializer
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
    

class ProjectCreateAPIView(generics.CreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsClient]

    def perform_create(self, serializer):
        serializer.save(
            client=self.request.user.client_profile
        )


class ProjectListAPIView(generics.ListAPIView):
    queryset = Project.objects.all().order_by("-created")
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]


class ProjectDetailRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
