from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from profiles.permissions import IsFreelancer
from proposals.api.v1.serializers import ProposalSerializer
from proposals.models import Proposal


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
