from django.db import models

class Reviewer(models.Model):
    """Model that describes a reviewer on the admission committee"""
    name = models.CharField(max_length=30)
