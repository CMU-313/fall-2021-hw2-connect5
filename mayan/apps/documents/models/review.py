from mayan.apps.documents.models.applicant import Applicant
from mayan.apps.documents.models.reviewer import Reviewer
from django.db import models

class Review(models.Model):
    """Model that describes a review"""
    reviewer = models.ForeignKey(to=Reviewer, on_delete=models.CASCADE)
    applicant = models.ForeignKey(to=Applicant, on_delete=models.CASCADE)
    # After discussing with Albert and James, we decided that the 
    # evaluation should be a serialized string of a dictionary
    # mapping from metric names to scores
    evaluation = models.TextField()
