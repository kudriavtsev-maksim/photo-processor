from django.db import models
import os

class ProcessedImage(models.Model):
    filename = models.CharField(max_length=255)
    original_filename = models.CharField(max_length=255)
    upload_time = models.DateTimeField(auto_now_add=True)
    result_number = models.IntegerField()
    processing_time = models.FloatField(default=0)
    
    def __str__(self):
        return f"{self.orginal_filename} - {self.reult_number}"
    