from django.db import models

class Projects(models.Model):
    title = models.CharField(max_length=256)
    image = models.ImageField()
    description = models.TextField()
    def __str__(self):
        return f'{self.title}'
