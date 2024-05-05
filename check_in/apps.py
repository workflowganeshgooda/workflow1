# apps.py
from django.apps import AppConfig

class SoftIssueConfig(AppConfig):
    name = 'check_in'  # Use underscores instead of hyphens
    verbose_name = 'Check In'
