from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from core.permissions import  IsFreelancer
from freelancers.models import FreelancerProfile, Proposal
from freelancers.api.v1.serializers import (  
    FreelancerProfileSerializer,
    FreelancerProfileDetailSerializer,
    ProposalSerializer,
    )
    

class FreelancerProfileCreateAPIView(generics.CreateAPIView):
    serializer_class = FreelancerProfileSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FreelancerProfileRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FreelancerProfileDetailSerializer
    permission_classes = [IsAuthenticated, IsFreelancer]
    
    def get_object(self):
        return get_object_or_404(FreelancerProfile, user=self.request.user)


class ProposalListAPIView(generics.ListAPIView):
    queryset = Proposal.objects.all().order_by("-created")
    serializer_class = ProposalSerializer
    permission_classes = [IsAuthenticated]


class ProposalCreateAPIView(generics.CreateAPIView):
    serializer_class = ProposalSerializer
    permission_classes = [IsAuthenticated, IsFreelancer]

    def perform_create(self, serializer):
        serializer.save(
            freelancer=self.request.user.freelancer_profile
        )
    

class ProposalRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer
