from django.urls import path
from profiles.api.v1.views import (
    ClientProfileCreateAPIView, 
    FreelancerProfileCreateAPIView,
    ClientProfileRetrieveUpdateDestroyAPIView,
    FreelancerProfileRetrieveUpdateDestroyAPIView,
    )

urlpatterns = [
    path("client-profile/", ClientProfileCreateAPIView.as_view(), name='my-client-profile'),
    path("client-profile-detail/", ClientProfileRetrieveUpdateDestroyAPIView.as_view(), name='my-client-profile-deatil'),
    path("freelancer-profile/", FreelancerProfileCreateAPIView.as_view(), name='my-freelancer-profile'),
    path("freelancer-profile-detail/", FreelancerProfileRetrieveUpdateDestroyAPIView.as_view(), name='my-freelancer-profile-deatil'),
]
