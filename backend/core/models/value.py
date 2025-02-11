"""EuroTempl System
Copyright (c) 2024 Pygmalion Records

ParameterValue model implementation for the EuroTempl system.
This model stores specific values for parameters in component instances.
"""

from django.db import models
from django.db.models import JSONField
from django.core.exceptions import ValidationError
import uuid

class ParameterValue(models.Model):
    """
    Stores specific values for parameters in component instances.
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        help_text="Unique identifier for the parameter value"
    )
    parameter = models.ForeignKey(
        'Parameter',
        on_delete=models.CASCADE,
        help_text="Reference to parameter definition"
    )
    instance = models.ForeignKey(
        'ComponentInstance',
        on_delete=models.CASCADE,
        help_text="Reference to component instance"
    )
    value = JSONField(
        help_text="The actual value of the parameter"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'et_parameter_value'
        indexes = [
            models.Index(fields=['parameter']),
            models.Index(fields=['instance']),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=['parameter', 'instance'],
                name='unique_parameter_value_per_instance'
            )
        ]

    def clean(self):
        """Validate the value against parameter constraints."""
        if self.parameter:
            self.parameter.validate_value(self.value)
        super().clean()

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)