from django.db import models

class VolunteerOpportunity(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

class VolunteerSignUp(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    opportunity = models.ForeignKey(VolunteerOpportunity, on_delete=models.CASCADE)
    date_signed_up = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} for {self.opportunity.title}"
