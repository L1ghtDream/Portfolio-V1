from django.db import models
from django.db.models import Model


class Entry(models.Model):
    type = models.CharField(max_length=10000)
    name = models.CharField(max_length=10000)
    description = models.TextField()
    image = models.CharField(max_length=10000)
    ip = models.CharField(max_length=10000, blank=True)
    #url = models.CharField(max_length=10000)

    def __str__(self):
        return f"{self.name} ({self.type})"

class SubEntry(models.Model):
    name = models.CharField(max_length=10000)
    url = models.CharField(max_length=10000, blank=True)
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE, related_name="subEntries")
    description = models.TextField(blank=True)
