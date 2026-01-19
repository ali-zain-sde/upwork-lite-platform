from django.urls import path
from profiles.api.v1.views import ClientProfileCreateAPIView, FreelancerProfileCreateAPIView

urlpatterns = [
    path('client-profile/', ClientProfileCreateAPIView.as_view(), name='client-profile'),
    path('freelancer-profile/', FreelancerProfileCreateAPIView.as_view(), name='freelancer-profile'),
]
