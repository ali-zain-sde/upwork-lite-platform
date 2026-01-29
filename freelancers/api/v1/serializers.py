from rest_framework import serializers
from freelancers.models import Proposal, Freelancer


class FreelancerCreateSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Freelancer
        fields = (
            "title",
            "hourly_rate",
            "bio",
            "portfolio_link",
            "skills",
        )


class FreelancerRetrieveUpdateSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Freelancer
        fields = (
            "id",
            "title",
            "hourly_rate",
            "bio",
            "portfolio_link",
            "skills",
        )
        read_only_fields = ("id",)


class ProposalCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = (
            "cover_letter",
            "proposed_rate",
        )


class ProposalListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = (
            "id",
            "cover_letter",
            "proposed_rate",
            "project_id",            
        )


class ProposalUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = (
            "id",
            "cover_letter",
            "proposed_rate",
            "created",
            "modified",
        )
        read_only_fields = ("id",)
