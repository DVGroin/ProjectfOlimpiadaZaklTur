from django.db import models

# Create your models here.

class UploadedAudio(models.Model):
    audio = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)