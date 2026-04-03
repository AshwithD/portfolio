
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # image = models.ImageField(upload_to='projects/')
    image = models.CharField(max_length=255)
    link = models.URLField()
    tech_stack = models.CharField(max_length=200)
    icon = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title