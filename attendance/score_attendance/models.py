from django.db import models

# Create your models here.
class Student(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    score = models.IntegerField(default=0)
    def __str__(self):
        return self.firstname + ' ' + self.lastname
