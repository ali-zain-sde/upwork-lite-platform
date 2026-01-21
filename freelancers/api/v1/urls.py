from django.urls import path
from freelancers.api.v1.views import (
    ProposalListAPIView,
    ProposalCreateAPIView,
    ProposalRetrieveAPIView,
    FreelancerProfileCreateAPIView,
    FreelancerProfileRetrieveUpdateDestroyAPIView,
    )

urlpatterns = [
    path('', ProposalListAPIView.as_view(), name='proposal-list'),
    path('proposal/', ProposalCreateAPIView.as_view(), name='proposal-create'),
    path('<str:id>/', ProposalRetrieveAPIView.as_view(), name='proposal-detail'),
    path("profile-view/", FreelancerProfileCreateAPIView.as_view(), name='profile-view'),
    path("profile-update/", FreelancerProfileRetrieveUpdateDestroyAPIView.as_view(), name='profile-update'),
]
