from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Song(models.Model):
    name = models.CharField(max_length=128, default="none")
    author = models.CharField(max_length=128, default="none")
    album = models.CharField(max_length=128, default="none")
    duration = models.CharField(max_length=128, default="none")

    def __str__(self):
        return self.name + " - " + self.author


class User(models.Model):
    userName = models.CharField(max_length=128, default="none")
    email = models.CharField(max_length=128, default="none")

    def __str__(self):
        return self.userName + " - " + self.email


class CollaborativeList(models.Model):
    name = models.CharField(max_length=128, default="none")
    songs = models.ManyToManyField(Song)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class Concert(models.Model):
    title = models.CharField(max_length=128, default="none")
    datetime = models.CharField(max_length=128, default="none")
    address = models.CharField(max_length=128, default="none")
    lat = models.DecimalField(decimal_places=7, max_digits=15, default=0.0)
    lon = models.DecimalField(decimal_places=7, max_digits=15, default=0.0)

    def __str__(self):
        return self.title + " - " + self.address + " - " + self.datetime


class Ticket(models.Model):
    zone = models.CharField(max_length=128, default="none")
    price = models.DecimalField(decimal_places=2, max_digits=6, default=0.0)
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE)

    def __str__(self):
        return self.zone + " - " + self.price


class DJSession(models.Model):
    sessionCode = models.CharField(max_length=7, default="0000000")
    queue = models.ManyToManyField(Song)
    sessionCreator = models.IntegerField(default=-1)
    sessionMembers = ArrayField(models.IntegerField(), default=list())

    def __str__(self):
        return "DJSession from: " + str(self.sessionCreator) + " (" + self.sessionCode + ")"