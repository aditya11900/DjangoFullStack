from django.db import models
from django.utils import timezone

# Create your models here.

class ProjectVariety(models.Model):
    PROJECT_TYPE = [
        ('web', 'Web Development'),
        ('mobile', 'Mobile Development'),
        ('desktop', 'Desktop Development'),
        ('game', 'Game Development'),
        ('other', 'Other Development'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="img/")
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=100, choices=PROJECT_TYPE)
    
    def __str__(self):
        return self.name
    
