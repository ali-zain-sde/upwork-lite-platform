from django.urls import path
from freelancers.api.v1.views import (
    FreelancerCreateAPIView,
    FreelancerRetrieveUpdateAPIView,
    ProposalCreateAPIView,
    ProposalListAPIView,
    ProposalRetrieveUpdateDestroyAPIView,
    )

urlpatterns = [
    # Freelancer profile (self)
    path("", FreelancerRetrieveUpdateAPIView.as_view()),
    path("create/", FreelancerCreateAPIView.as_view()),

    # create proposal against a project
    path("<uuid:pk>/", ProposalCreateAPIView.as_view()),

    # list freelancer own proposals (freelancer dashboard)
    path("proposals/", ProposalListAPIView.as_view()),

    # retrieve/update freelancer his own proposal
    path("proposals/<uuid:pk>/", ProposalRetrieveUpdateDestroyAPIView.as_view()),
]
