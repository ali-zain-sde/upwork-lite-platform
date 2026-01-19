from rest_framework import serializers
from users.models import User, Profile


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    phone = serializers.CharField(write_only=True)
    date_of_birth = serializers.DateField(write_only=True)
    gender = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "password",
            "phone",
            "date_of_birth",
            "gender"
        ]

    def create(self, validated_data):
        profile_data = {
            "phone": validated_data.pop("phone"),
            "date_of_birth": validated_data.pop("date_of_birth"),
            "gender": validated_data.pop("gender")
        }
        user = User.objects.create_user(**validated_data)
        Profile.objects.create(user=user, **profile_data)

        return user


class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='user.email', read_only=True)
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)
    password = serializers.CharField(source='user.password', read_only=True)

    class Meta: 
        model = Profile
        fields = [
            "first_name",
            "last_name",
            "email",
            "password",
            "phone",
            "date_of_birth",
            "gender"
        ]
