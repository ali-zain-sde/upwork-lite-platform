from rest_framework import serializers
from freelancers.models import Proposal, FreelancerProfile


class FreelancerProfileDetailSerializer(serializers.ModelSerializer):
    class Meta: 
        model = FreelancerProfile
        

class FreelancerProfileSerializer(FreelancerProfileDetailSerializer):
    def validate(self, attrs):
        user = self.context["request"].user
        if FreelancerProfile.objects.filter(user=user).exists():
            raise serializers.ValidationError("Freelancer profile already exists.")
        return attrs


class ProposalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Proposal
        fields = '__all__'
