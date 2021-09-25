from mayan.apps.documents.models.document_file_models import DocumentFile
from django.db import models

class Applicant(models.Model):
    """Model that describes a grad school applicant"""
    name = models.TextField()
    resume = models.ForeignKey(to=DocumentFile, on_delete=models.CASCADE)
