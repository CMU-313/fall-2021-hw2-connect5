from mayan.apps.documents.models.document_file_models import DocumentFile
from django.db import models

class Metric(models.Model):
    """Model that describes a metric"""
    metric_name = models.TextField()
    metric_type = models.TextField()
