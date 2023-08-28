from django.db import models


class Business(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=5000)
    category = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone1 = models.CharField(max_length=100)
    phone2 = models.CharField(max_length=100)
    location = models.CharField(max_length= 100)
    images = models.CharField(max_length= 100)
    ratings = models.CharField(max_length= 100)
    reviews = models.CharField(max_length= 100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey('auth.User', related_name='business', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']