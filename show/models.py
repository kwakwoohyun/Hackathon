from django.db import models

# Create your models here.
class Show(models.Model):
    name = models.CharField(max_length=30)
    info = models.TextField()
    google_map = models.CharField(max_length=200)
    poster = models.CharField(max_length=200)
    go = models.TextField()
    video = models.CharField(max_length=200)

    def __str__(self):
        return self.name
