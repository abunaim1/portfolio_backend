from django.db import models

# Create your models here.

class ContactModel(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f'Name: {self.name} Subject: {self.subject}'