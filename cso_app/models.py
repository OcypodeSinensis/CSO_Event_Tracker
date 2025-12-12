from django.db import models

class CSOEvent(models.Model):
    location = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    overflow_volume_m3 = models.FloatField()
    cause = models.CharField(max_length=255)
    severity = models.CharField(max_length=50)
    description = models.TextField(blank=True)

class MitigationAction(models.Model):
    cso_event = models.ForeignKey(CSOEvent, on_delete=models.CASCADE)
    action_type = models.CharField(max_length=255)
    completion_date = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)
