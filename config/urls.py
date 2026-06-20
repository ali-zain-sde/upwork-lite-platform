from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/users/', include("users.api.v1.urls")),
    path('api/v1/clients/', include("clients.api.v1.urls")),
    path('api/v1/freelancers/', include("freelancers.api.v1.urls")),
]
