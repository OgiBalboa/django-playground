from django.db import models
from django.utils.module_loading import import_string

from core.models import BaseModel


class ValueCalculator(BaseModel):
    library = models.CharField(max_length=250)
    is_active = models.BooleanField()
    config = models.JSONField(default=dict)

    def calculate(self, values):
        calculator_class = import_string(self.library)
        calculator = calculator_class(**values)
        return calculator.result

