from django.db import models
from django.contrib.auth import get_user_model
from core.models import BaseModel

User = get_user_model()


class Client(BaseModel):
    company_name = models.CharField(max_length=255)
    company_website = models.URLField(blank=True)

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='client'
    )


class Project(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    is_open = models.BooleanField(default=True)

    client = models.ForeignKey(
        "clients.Client",
        on_delete=models.CASCADE,
        related_name="projects"
    )

    class Meta:
        ordering = ["-is_open", "-created"]
