from django.db import models
from core.models import BaseModel
from projects.models import Project
from profiles.models import FreelancerProfile

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
        