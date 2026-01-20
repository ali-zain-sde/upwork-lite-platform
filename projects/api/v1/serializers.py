from rest_framework import serializers
from projects.models import Project
from proposals.api.v1.serializers import ProposalSerializer


class ProjectSerializer(serializers.ModelSerializer):
    proposals = ProposalSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = "__all__"
        