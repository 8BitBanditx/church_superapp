from django.db import models

class PrayerRequest(models.Model):
    name = models.CharField(max_length=100)
    request = models.TextField()
    date_submitted = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=False)
    answered = models.BooleanField(default=False)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.request[:30]}..."
