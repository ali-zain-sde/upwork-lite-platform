from django.urls import path
from clients.api.v1.views import (
    ProjectListAPIView,
    ProjectRetrieveAPIView,
    ProjectCreateAPIView,
    ProjectRetrieveUpdateDestroyAPIView,
    ClientCreateAPIView,
    ClientRetrieveUpdateAPIView,
    ProjectProposalListAPIView,
    )

urlpatterns = [
    # Client profile (self) 
    path("", ClientRetrieveUpdateAPIView.as_view()),   
    path("create/", ClientCreateAPIView.as_view()),

    #Public API - All Projects listing and also project detail by retreiving
    path("projects/", ProjectListAPIView.as_view()),
    path("projects/<uuid:pk>/", ProjectRetrieveAPIView.as_view()),

    # API for clients to create and update there projects
    path("projects/create/", ProjectCreateAPIView.as_view()),
    path("projects/<uuid:pk>/manage/", ProjectRetrieveUpdateDestroyAPIView.as_view()),

    # API for Client to see proposals on his project
    path("projects/<uuid:pk>/proposals/", ProjectProposalListAPIView.as_view()),
]
