from django.db import models

class Flower(models.Model):
    name = models.CharField(max_length=60)
    color = models.CharField(max_length=60)
    season = models.CharField(max_length=60)

    def __str__(self):
        return f'{self.name} {self.color} | {self.season}'