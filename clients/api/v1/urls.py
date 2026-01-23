from django.urls import path
from clients.api.v1.views import (
    ProjectListCreateAPIView,
    ProjectDetailRetrieveAPIView,
    ClientCreateAPIView, 
    ClientRetrieveUpdateDestroyAPIView,
    )

urlpatterns = [
    path('projects/', ProjectListCreateAPIView.as_view(), name='projects'),
    path('projects/<uuid:pk>/', ProjectDetailRetrieveAPIView.as_view(), name='project_detail'),
    path("profile/", ClientCreateAPIView.as_view(), name='client_profile'),
    path("profile/me/", ClientRetrieveUpdateDestroyAPIView.as_view(), name='client_profile_update'),
]
