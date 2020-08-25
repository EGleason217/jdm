from django.db import models

class Shoots(models.Model):
    image = models.ImageField(upload_to='static/imgs/')
    description = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
