from django.db import models
from datetime import datetime

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if postData['title'] == '' or len(postData['title']) < 2:
            errors['title'] = 'Title field should be at least 2 characters'
        if postData['network'] == '' or len(postData['network']) < 3:
            errors['network'] = 'Network field should be at least 3 characters'
        if postData['description'] == '' or len(postData['description']) < 10:
            errors['description'] = 'Description should be at least 10 characters'
        if datetime.strptime(postData['date'], '%Y-%m-%d') > datetime.now():
            errors['date'] = 'Invalid release date'
        return errors


class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
    

