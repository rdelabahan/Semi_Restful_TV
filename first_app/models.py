from django.db import models
from datetime import datetime

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if postData['title'] == '' or len(postData['title']) < 2 or len(postData['title']) > 255:
            errors['title'] = 'Title field should have 2 characters to 255 characters long'
        if postData['network'] == '' or len(postData['network']) < 3 or len(postData['network']) > 255:
            errors['network'] = 'Network field should have 3 characters to 255 characters long'
        if postData['description'] == '' or len(postData['description']) < 10 or len(postData['description']) > 255:
            errors['description'] = 'Description should have 10 characters to 255 characters long'
        try:   
            if postData['date'] == '' or datetime.strptime(postData['date'], '%Y-%m-%d') > datetime.now():
                errors['date'] = 'Invalid release date'
        except:
            pass
        # try:
        #     Show.objects.get(title = postData['title'])
        #     errors['title'] = 'Show name already exists'
        # except:
        #     pass
        if len(Show.objects.filter(title = postData['title'])) >= 1:
            errors['title'] = 'Show name already exists'
        return errors


class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
    

