from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/users/', include("users.api.v1.urls")),
    path('api/v1/profiles/', include("profiles.api.v1.urls")),
]
