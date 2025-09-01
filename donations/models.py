from django.db import models

class Donation(models.Model):
    DONATION_METHODS = [
        ('envelope', 'Envelope'),
        ('cash', 'Cash'),
        ('online', 'Online'),
        ('check', 'Check'),
    ]
    donor_name = models.CharField(max_length=100)
    envelope_number = models.CharField(max_length=50, blank=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    method = models.CharField(max_length=20, choices=DONATION_METHODS)
    date = models.DateField(auto_now_add=True)
    note = models.TextField(blank=True)

    def __str__(self):
        return f"{self.donor_name} - ${self.amount} ({self.method})"
