from django.db import models

class Python(models.Model):
    heading = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.heading

