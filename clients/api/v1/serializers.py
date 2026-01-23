from rest_framework import serializers
from clients.models import Client, Project
from freelancers.api.v1.serializers import ProposalDetailSerializer, ProposalMiniSerializer


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = (
            "company_name",
            "company_website",
        )


class ProjectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            "title",
            "budget",
            "description",
        )
    

class ProjectListSerializer(serializers.ModelSerializer):
    proposals = ProposalMiniSerializer(many=True, read_only=True)
    class Meta:
        model = Project
        fields = (
            "id",
            "title",
            "budget",
            "is_open",
            "proposals",
        )
        read_only_fields = ("id",)


class ProjectDetailSerializer(serializers.ModelSerializer):
    proposals = ProposalDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = (
            "id",
            "title",
            "description",
            "budget",
            "is_open",
            "proposals",
        )
        read_only_fields = ("id",)
