from django.db import models
from django.conf import settings
from datetime import datetime
from django.db import models
from datetime import datetime

class SoftwareIssue(models.Model):
    req_by = models.CharField(max_length=255)
    req_by_id = models.CharField(max_length=255)
    req_type = models.CharField(max_length=255)
    approved = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)
    closed = models.BooleanField(default=False)
    approved_timestamp = models.DateTimeField(null=True, blank=True)  # New field for approved timestamp
    rejected_timestamp = models.DateTimeField(null=True, blank=True)  # New field for rejected timestamp
  
    email = models.EmailField()
    desc = models.TextField()
    file1 = models.FileField(upload_to='uploads/')
    att = models.ImageField(upload_to='uploads/')
    status = models.BooleanField(default=True)
    datadeleted = models.BooleanField(default=False)
    timestamp = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"Software Issue #{self.id} - Requested by {self.req_by} at {self.timestamp}"


class AuditLogSoftwareIssue(models.Model):
    ACTION_CHOICES = (
        ('create', 'Create'),
        ('update', 'Update'),
        ('delete', 'Delete'),
        ('restore', 'Restore'),  # Add the "restore" action
    )

    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    model_name = models.CharField(max_length=255)
    record_id = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(default=datetime.now)
    username = models.CharField(max_length=255)  # Field for username
    previous_data = models.TextField(blank=True, null=True)  # Field for previous data
    new_data = models.TextField(blank=True, null=True)  # Field for new data

    def __str__(self):
        return f'{self.action} on {self.model_name} (ID: {self.record_id}) by {self.user} at {self.timestamp}'
