from django.db import models

class Metric(models.Model):
    """Model that describes a metric"""
    metric_name = models.CharField(max_length=30)
