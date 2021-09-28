from mayan.apps.documents.models.document_models import Document
from django.db import models

class Applicant(models.Model):
    """Model that describes a grad school applicant"""
    name = models.CharField(max_length=30)
    document = models.ForeignKey(to=Document, on_delete=models.CASCADE)
