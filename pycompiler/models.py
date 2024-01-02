from django.db import models
from django.contrib.auth.models import User

class Code(models.Model):
    code = models.TextField()
    output = models.TextField()
# Create your models here.
    


class Student(models.Model):
    rollno = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True, unique = True)



class Faculty(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)