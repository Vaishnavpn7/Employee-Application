from django.db import models


class Employees(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.PositiveIntegerField()

    def __str__(self):
        return self.name
