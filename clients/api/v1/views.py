from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework import generics
from rest_framework.permissions import AllowAny
from clients.models import Client, Project
from clients.api.v1.serializers import (
    ClientCreateSerializer,
    ClientRetreiveUpdateSerializer,
    ProjectCreateSerializer,
    ProjectUpdateSerializer,
    ProjectRetrieveSerializer,
    ProjectListSerializer,
    ProjectProposalSerializer,
    )


class ClientCreateAPIView(generics.CreateAPIView):
    serializer_class = ClientCreateSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ClientRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = ClientRetreiveUpdateSerializer
    
    def get_object(self):
        return get_object_or_404(Client, user=self.request.user)
   

class ProjectCreateAPIView(generics.CreateAPIView):
    serializer_class = ProjectCreateSerializer

    def perform_create(self, serializer):
        serializer.save(
            client=self.request.user.client
        )


class ProjectListAPIView(generics.ListAPIView):
    serializer_class = ProjectListSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Project.objects.filter(
            Q(status="open") | Q(status="draft")
        )
    

class ProjectRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ProjectRetrieveSerializer    
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Project.objects.filter(
        id=self.kwargs["pk"]
    )


class ProjectRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectUpdateSerializer

    def get_queryset(self):
        return Project.objects.filter(
            client=self.request.user.client,
        )
    

class ProjectProposalListAPIView(generics.ListAPIView):
    serializer_class = ProjectProposalSerializer

    def get_queryset(self):
        return Project.objects.filter(
            client=self.request.user.client,
        )
