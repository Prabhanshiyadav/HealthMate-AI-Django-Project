from django.db import models

class HealthEntry(models.Model):
    date = models.DateField()
    weight = models.FloatField()
    steps = models.IntegerField(default=0)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.date} - {self.weight}kg"
