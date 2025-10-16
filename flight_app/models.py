from django.db import models

class Airport(models.Model):
    code = models.CharField(max_length=5, unique=True)

    def __str__(self):
        return self.code


class Route(models.Model):
    DIRECTION_CHOICES = [
        ('Left', 'Left'),
        ('Right', 'Right'),
    ]

    source = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='source_routes')
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='destination_routes')
    position = models.CharField(max_length=10, choices=DIRECTION_CHOICES)
    duration = models.IntegerField(help_text="Distance in KM")

    def __str__(self):
        return f"{self.source} → {self.destination} ({self.position}, {self.duration} KM)"
