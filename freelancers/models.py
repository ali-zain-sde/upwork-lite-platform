from django.db import models
from users.models import User
from core.models import BaseModel
from clients.models import Project
from freelancers.models import FreelancerProfile


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


class Proposal(BaseModel):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="proposals"
    )
    freelancer = models.ForeignKey(
        FreelancerProfile,
        on_delete=models.CASCADE,
        related_name="proposals"
    )
    cover_letter = models.TextField()
    proposed_rate = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["project", "freelancer"],
                name="unique_proposal_per_project_per_freelancer"
            )
        ]
        