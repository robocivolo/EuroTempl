from django.contrib.gis.db import models

class ComponentInstance(models.Model):
    component = models.ForeignKey('core.Component', on_delete=models.PROTECT)
    location = models.GeometryField(dim=3, srid=4326)
    properties = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']