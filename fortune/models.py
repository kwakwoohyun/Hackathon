from django.db import models

# Create your models here.

class Fortune(models.Model):
<<<<<<< HEAD
    show_id = models.IntegerField()
    date = models.DateTimeField()
    time = models.DateTimeField()
    number = models.IntegerField()
    finish = models.DateTimeField()

    entries = models.ManyToManyField("User", blank=True)

    def __str__(self):
        return self.title

class UserFortune(models.Model):
    fortune_id = models.ForeignKey(
        Fortune, on_delete=models.CASCADE, related_name="users")
    user_id = models.IntegerField()

    def __str__(self):
        return self.user_id
=======

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
>>>>>>> 6e49c60dd83a0898ea83013f472a5d010eb9cec4
