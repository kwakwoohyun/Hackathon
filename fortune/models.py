from django.db import models

# Create your models here.

class Fortune(models.Model):
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