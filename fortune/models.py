from django.db import models

# Create your models here.

class Fortune(models.Model):
    show_id = models.IntegerField()
    date = models.CharField(max_length=500)
    price = models.CharField(max_length=500)
    starttime = models.CharField(max_length=500)
    finishtime = models.CharField(max_length=500)
    number = models.IntegerField()
    calcuatetime = models.CharField(max_length=500)

class User(models.Model):
    fortune_id = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.user_id
