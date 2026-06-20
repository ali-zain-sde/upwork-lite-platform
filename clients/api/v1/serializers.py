from rest_framework import serializers
from clients.models import Client, Project
from freelancers.models import Proposal


class ClientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = (
            "full_name",
            "phone",
            "company_name",
            "company_website",
        )


class ClientRetreiveUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = (
            "id",
            "full_name",
            "phone",
            "company_name",
            "company_website",
        )
        read_only_fields = ("id",)


class ProjectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            "id",
            "title",
            "budget",
            "description",
        )
        read_only_fields = ("id",)
    

class ProjectRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            "id",
            "title",
            "description",
            "budget",
            "status",
        )
        read_only_fields = ("id",)


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            "id",
            "title",
            "budget",
            "status",
        )
        read_only_fields = ("id",)


class ProjectUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            "id",
            "title",
            "description",
            "budget",
            "status",
        )
        read_only_fields = ("id",)


class ProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = (
            "id",
            "freelancer",
            "cover_letter",
            "proposed_rate",
        )
        read_only_fields = ("id",)


class ProjectProposalSerializer(serializers.ModelSerializer):
    proposals = ProposalSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = (
            "id",
            "title",
            "description",
            "budget",
            "status",
            "proposals",
        )
        read_only_fields = ("id",)
