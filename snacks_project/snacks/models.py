from django.db import models

# Create your models here.

class Snack(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    calories = models.IntegerField()
    

    def __str__(self):
        return self.name
        

