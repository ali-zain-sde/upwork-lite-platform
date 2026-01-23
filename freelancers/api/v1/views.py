from django.shortcuts import get_object_or_404
from rest_framework import generics
from freelancers.models import Freelancer, Proposal
from clients.models import Project
from freelancers.api.v1.serializers import (  
    FreelancerSerializer,
    ProposalDetailSerializer,
    ProposalMiniSerializer,
    )
    

class FreelancerCreateAPIView(generics.CreateAPIView):
    serializer_class = FreelancerSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FreelancerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FreelancerSerializer
    
    def get_object(self):
        return get_object_or_404(Freelancer, user=self.request.user)


class ProposalListCreateAPIView(generics.ListCreateAPIView):
    def perform_create(self, serializer):
        serializer.save(
            freelancer=self.request.user.freelancer,
            project=get_object_or_404(Project, id=self.kwargs["project_id"])
        )

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ProposalDetailSerializer
        else:
            return ProposalMiniSerializer

    def get_queryset(self):
        return Proposal.objects.filter(
            project_id=self.kwargs["project_id"]
        )


class ProposalRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Proposal.objects.all()
    serializer_class = ProposalDetailSerializer
