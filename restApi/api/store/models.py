from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=255)
    prize = models.IntegerField(null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name