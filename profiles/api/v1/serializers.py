from rest_framework import serializers
from profiles.models import ClientProfile, FreelancerProfile


class ClientProfileSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ClientProfile
        exclude = ("user",)

    def create(self, validated_data):
        user = self.context["request"].user
        if hasattr(user, "client_profile"):
            raise serializers.ValidationError("Client profile already exists.")
        return ClientProfile.objects.create(user=user,**validated_data)

class FreelancerProfileSerializer(serializers.ModelSerializer):
    class Meta: 
        model = FreelancerProfile
        exclude = ("user",)

    def create(self, validated_data):
        user = self.context["request"].user
        if hasattr(user, "freelancer_profile"):
            raise serializers.ValidationError("Freelancer profile already exists.")
        return FreelancerProfile.objects.create(user=user,**validated_data)
    