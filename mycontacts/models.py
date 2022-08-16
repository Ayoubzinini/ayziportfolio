from distutils.command.upload import upload
from email.mime import image
from pydoc import describe
from django.db import models

class Contact(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    description = models.TextField(null=True)
    def __str__(self):
        return self.summary