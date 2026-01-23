from django.db import models
from django.contrib.auth import get_user_model
from core.models import BaseModel

User = get_user_model()


class Freelancer(BaseModel):
    title = models.CharField(max_length=255)
    skills = models.TextField()
    hourly_rate = models.DecimalField(max_digits=8, decimal_places=2)
    bio = models.TextField()
    portfolio_link = models.URLField(blank=True)

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='freelancer',
    )


class Proposal(BaseModel):
    cover_letter = models.TextField()
    proposed_rate = models.DecimalField(max_digits=10, decimal_places=2)

    project = models.ForeignKey(
        "clients.Project",
        on_delete=models.CASCADE,
        related_name="proposals",
    )
    freelancer = models.ForeignKey(
        "freelancers.Freelancer",
        on_delete=models.CASCADE,
        related_name="proposals"
    )

    class Meta:
        ordering = ["-created"]
