from django.db import models

# Create your models here.
class Addstudent(models.Model):
    # ...
    def __str__(self):
        return self.name
class Addemployee(models.Model):
    # ...
    def __str__(self):
        return self.name

