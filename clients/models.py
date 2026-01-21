from django.db import models
from users.models import User
from core.models import BaseModel
from clients.models import ClientProfile


class ClientProfile(BaseModel):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='client_profile'
    )
    company_name = models.CharField(max_length=255)
    company_website = models.URLField(blank=True)


class Project(BaseModel):
    client = models.ForeignKey(
        ClientProfile,
        on_delete=models.CASCADE,
        related_name="clients"
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    is_open = models.BooleanField(default=True)
