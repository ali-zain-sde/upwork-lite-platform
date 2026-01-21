from rest_framework import serializers
from clients.models import ClientProfile, Project
from freelancers.api.v1.serializers import ProposalSerializer


class ClientProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientProfile
        exclude = ("user",)
        read_only_fields = ("id",)
    

class ClientProfileSerializer(ClientProfileDetailSerializer):
    def validate(self, attrs):
        user = self.context["request"].user
        if ClientProfile.objects.filter(user=user).exists():
            raise serializers.ValidationError("Client profile already exists.")
        return attrs


class ProjectSerializer(serializers.ModelSerializer):
    proposals = ProposalSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = "__all__"
