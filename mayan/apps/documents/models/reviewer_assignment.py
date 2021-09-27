from mayan.apps.documents.models.applicant import Applicant
from mayan.apps.documents.models.reviewer import Reviewer

from django.db import models

class ReviewerAssignment(models.Model):
    """Model that describes a reviewer-application assignment"""
    reviewer = models.ForeignKey(to=Reviewer, on_delete=models.CASCADE)
    applicant = models.ForeignKey(to=Applicant, on_delete=models.CASCADE)
