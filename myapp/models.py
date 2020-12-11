from django.db import models

# Create your models here.
class Song (models.Model):
    name = models.CharField
    author = models.CharField
    album = models.CharField
    duration = models.IntegerField

    def __str__(self):
        return self.name + " - " + self.author

class User (models.Model):
    userName = models.CharField
    email = models.CharField

    def __str__(self):
        return self.userName + " - " + self.email
    

class CollaborativeList (models.Model):
    songs = models.ManyToManyField(Song)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.songs + "\n" + self.users
