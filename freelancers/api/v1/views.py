from django.shortcuts import get_object_or_404
from rest_framework import generics
from freelancers.models import Freelancer, Proposal
from clients.models import Project
from freelancers.api.v1.serializers import (  
    FreelancerCreateSerializer,
    FreelancerRetrieveUpdateSerializer,
    ProposalUpdateSerializer,
    ProposalCreateSerializer,
    ProposalListSerializer,
    )
    
    
class FreelancerCreateAPIView(generics.CreateAPIView):
    serializer_class = FreelancerCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FreelancerRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = FreelancerRetrieveUpdateSerializer
            
    def get_object(self):
        return get_object_or_404(Freelancer, user=self.request.user)


class ProposalListAPIView(generics.ListAPIView):
    serializer_class = ProposalListSerializer

    def get_queryset(self):
        return Proposal.objects.filter(
            freelancer=self.request.user.freelancer
        )


class ProposalCreateAPIView(generics.CreateAPIView):
    serializer_class = ProposalCreateSerializer
    
    def perform_create(self, serializer):
        serializer.save(
            freelancer=self.request.user.freelancer,
            project=Project.objects.get(id=self.kwargs["pk"])
        )


class ProposalRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProposalUpdateSerializer

    def get_queryset(self):
        return Proposal.objects.filter(
            freelancer=self.request.user.freelancer
        )
