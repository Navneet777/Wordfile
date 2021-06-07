from django.db import models

# Create your models here.
class FileModel(models.Model):
    word_file = models.FileField(blank=True, upload_to='media')
