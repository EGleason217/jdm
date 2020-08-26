from django.db import models

class Shoots(models.Model):
    image = models.ImageField(upload_to='static/imgs/')
    description = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Clients(models.Model):
    name = models.CharField(max_length=120)
    phone = models.IntegerField()
    email = models.EmailField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Locations(models.Model):
    client = models.ManyToManyField(Clients,related_name='locations')
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=2)
    zipcode = models.IntegerField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

