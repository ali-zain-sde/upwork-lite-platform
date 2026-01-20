from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from profiles.permissions import IsClient
from projects.api.v1.serializers import ProjectSerializer
from projects.models import Project


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
