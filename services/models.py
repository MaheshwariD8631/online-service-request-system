from django.db import models
from django.utils import timezone

class ServiceRequest(models.Model):
    PRIORITY = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    STATUS = [
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.CharField(max_length=100)
    service_type = models.CharField(max_length=100)
    description = models.TextField()
    priority = models.CharField(max_length=10, choices=PRIORITY, default='Medium')
    status = models.CharField(max_length=15, choices=STATUS, default='Open')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - {self.service_type}"

