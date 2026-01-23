from rest_framework import serializers
from freelancers.models import Proposal, Freelancer


class FreelancerSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Freelancer
        fields = (
            "title",
            "skills",
            "hourly_rate",
            "bio",
            "portfolio_link",
        )
    

class ProposalDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = (
            "id",
            "freelancer",
            "project",
            "cover_letter",
            "proposed_rate",
            "created",
            "modified",
        )
        read_only_fields = (
            'id',
            'freelancer',
            'project',
            "created",
            "modified",
        )


class ProposalMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = (
            "id",
            "project",
            "proposed_rate", 
            "freelancer",
            )
        read_only_fields = (
            "id", 
            "freelancer",            
            )
    