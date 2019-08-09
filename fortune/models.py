from django.db import models

# Create your models here.

class Fortune(models.Model):
<<<<<<< HEAD
=======

>>>>>>> 1230a10ab1f50034f70a0d86a306252d552edd35
    show_id = models.IntegerField()
    date = models.CharField(max_length=500)
    price = models.CharField(max_length=500)
    starttime = models.CharField(max_length=500)
    finishtime = models.CharField(max_length=500)
    number = models.IntegerField()
    seat = models.CharField(max_length=500)
    calcuatetime = models.CharField(max_length=500)

class User(models.Model):
    fortune_id = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.user_id
