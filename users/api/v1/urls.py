from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from users.api.v1.views import (
    UserRegisterCreateAPIView,
    UserLoginAPIView, 
    ProfileRetrieveUpdateAPIView,
    )

urlpatterns = [
    path('register/', UserRegisterCreateAPIView.as_view(), name='register'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile', ProfileRetrieveUpdateAPIView.as_view(), name='profile'),
]
