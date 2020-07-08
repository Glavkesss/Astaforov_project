from django.db import models

# Create your models here.


class Project(models.Model):
    PROJECT_TYPE = (
        ('coding', 'Программная разработка'),
        ('design', 'Разработка дизайна'),
        ('fullstuck', 'Полная разработка'),
    )
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1500)
    price = models.FloatField()

    def __str__(self):
        return f'title - {self.title}'