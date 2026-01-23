from django.urls import path
from freelancers.api.v1.views import (
    ProposalListCreateAPIView,
    ProposalRetrieveAPIView,
    FreelancerCreateAPIView,
    FreelancerRetrieveUpdateDestroyAPIView,
    )

urlpatterns = [
    path('projects/<uuid:project_id>/proposals/', ProposalListCreateAPIView.as_view(), name='project_proposals'),
    path('proposals/create/', ProposalListCreateAPIView.as_view(), name='proposal_create'),
    path('proposals/<uuid:pk>/', ProposalRetrieveAPIView.as_view(), name='proposal_detail'),
    path("profile/", FreelancerCreateAPIView.as_view(), name='freelancer_profile'),
    path("profile/me/", FreelancerRetrieveUpdateDestroyAPIView.as_view(), name='freelancer_profile_update'),
]
