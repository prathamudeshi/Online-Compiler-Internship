from django.db import models


class Code(models.Model):
    code = models.TextField()
    output = models.TextField()
# Create your models here.
