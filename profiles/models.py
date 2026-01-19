from django.db import models
from users.models import User
from core.models import BaseModel


class ClientProfile(BaseModel):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='client_profile'
    )
    company_name = models.CharField(max_length=255)
    company_website = models.URLField(blank=True)


class FreelancerProfile(BaseModel):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='freelancer_profile'
    )
    title = models.CharField(max_length=255)
    skills = models.TextField()
    hourly_rate = models.DecimalField(max_digits=8, decimal_places=2)
    bio = models.TextField()
    portfolio_link = models.URLField(blank=True)
