from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    phone_number = models.FloatField()
    instagram = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)

    def __str__(self):
        return f'name - {self.name}'