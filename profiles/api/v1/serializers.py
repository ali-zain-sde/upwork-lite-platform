from rest_framework import serializers
from profiles.models import ClientProfile, FreelancerProfile


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


class FreelancerProfileDetailSerializer(serializers.ModelSerializer):
    class Meta: 
        model = FreelancerProfile
        exclude = ("user",)
        read_only_fields = ("id",)


class FreelancerProfileSerializer(FreelancerProfileDetailSerializer):
    def validate(self, attrs):
        user = self.context["request"].user
        if FreelancerProfile.objects.filter(user=user).exists():
            raise serializers.ValidationError("Freelancer profile already exists.")
        return attrs
