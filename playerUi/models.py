from django.db import models
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

# Create your models here.
class Song(models.Model):
    SONG_TYPE_CHOICES = [
        ('OR', 'Original'),
        ('CV', 'Cover'),
        ('RM', 'Remix'),
    ]

    title = models.CharField(max_length=255)
    singer = models.CharField(max_length=255)
    release_date = models.DateField(null=True, blank=True)
    song_type = models.CharField(max_length=2, choices=SONG_TYPE_CHOICES, null=True, blank=True)

    # is_album = models.CharField(max_length=255,null=True, blank=True)
    # album_title = models.CharField(max_length=255, null=True, blank=True)
    # email = models.EmailField(max_length=255, null=True, blank=True)
    # country = models.CharField(max_length=255, null=True, blank=True)
    # note = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.title} by {self.singer}'
