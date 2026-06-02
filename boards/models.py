from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # One-to-Many: The creator of the project
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_projects')
    
    # Many-to-Many: Other users who can see/edit this project
    collaborators = models.ManyToManyField(User, related_name='shared_projects', blank=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    STATUS_CHOICES = [
        ('TODO', 'To Do'),
        ('IN_PROGRESS', 'In Progress'),
        ('DONE', 'Done'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='TODO')
    due_date = models.DateField(null=True, blank=True)
    
    # One-to-Many: Belongs to a single project
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    
    # One-to-Many: Assigned to a single user (optional)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_tasks')

    def __str__(self):
        return f"{self.title} ({self.status})"