from django.shortcuts import get_object_or_404
from rest_framework import generics
from clients.models import Client, Project
from clients.api.v1.serializers import (
    ClientSerializer,
    ProjectListSerializer,
    ProjectDetailSerializer,
    ProjectCreateSerializer,
    )


class ClientCreateAPIView(generics.CreateAPIView):
    serializer_class = ClientSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ClientRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClientSerializer

    def get_object(self):
        return get_object_or_404(Client, user=self.request.user)
    

class ProjectListCreateAPIView(generics.ListCreateAPIView):
    def get_queryset(self):
        return Project.objects.all()

    def perform_create(self, serializer):
        serializer.save(
            client=self.request.user.client
        )
    
    def get_serializer_class(self):
        if self.request.method == "POST":
            return ProjectCreateSerializer
        else:
            return ProjectListSerializer


class ProjectDetailRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer
