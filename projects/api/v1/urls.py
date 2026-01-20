from django.urls import path
from projects.api.v1.views import ProjectCreateAPIView, ProjectListAPIView, ProjectDetailRetrieveAPIView

urlpatterns = [
    path('', ProjectListAPIView.as_view(), name='project-list'),
    path('create/', ProjectCreateAPIView.as_view(), name='project-create'),
    path('<str:pk>/', ProjectDetailRetrieveAPIView.as_view(), name='project-detail'),
]
