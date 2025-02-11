from django.db import models

class Parameter(models.Model):
    component = models.ForeignKey('core.Component', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    value = models.JSONField()
    unit = models.CharField(max_length=50, blank=True)
    
    class Meta:
        ordering = ['name']