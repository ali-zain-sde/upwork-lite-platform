from django.urls import path
from clients.api.v1.views import (
    ProjectListAPIView,
    ProjectCreateAPIView,
    ProjectDetailRetrieveAPIView,
    ClientProfileCreateAPIView, 
    ClientProfileRetrieveUpdateDestroyAPIView,
    )

urlpatterns = [
    path('', ProjectListAPIView.as_view(), name='project-list'),
    path('project/', ProjectCreateAPIView.as_view(), name='project-create'),
    path('<str:pk>/', ProjectDetailRetrieveAPIView.as_view(), name='project-detail'),
    path("profile-view/", ClientProfileCreateAPIView.as_view(), name='profile-view'),
    path("profile-update/", ClientProfileRetrieveUpdateDestroyAPIView.as_view(), name='profile-update'),
]
