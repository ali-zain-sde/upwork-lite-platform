from django.db import models
from core.models import BaseModel
from profiles.models import ClientProfile


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
