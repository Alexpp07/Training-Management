from django.db import models

# Create your models here.
class Athlete(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=200)
    phoneNumber = models.IntegerField()
    email = models.CharField(max_length=100)
    birthday = models.DateField()

class Coach(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=200)
    phoneNumber = models.IntegerField()
    email = models.CharField(max_length=100)
    birthday = models.DateField()

class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

class AssociateAthleteGroup(models.Model):
    athleteId = models.ForeignKey(Athlete, on_delete=models.CASCADE)
    groupId = models.ForeignKey(Group, on_delete=models.CASCADE)

class AssociateCoachGroup(models.Model):
    athleteId = models.ForeignKey(Coach, on_delete=models.CASCADE)
    groupId = models.ForeignKey(Group, on_delete=models.CASCADE)