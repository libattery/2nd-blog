# Create your models here.
from django.db import models
from django.utils import timezone

class ConversionLog(models.Model):
    hwp_eq = models.CharField(max_length=500)
    latex_eq = models.CharField(max_length=500)
    created_date = models.DateTimeField(default=timezone.now)
    conversion_ok = models.BooleanField(default=True)

    def log_no_good(self):
        self.conversion_ok = False
        self.save()

    def __str__(self):
        return self.hwp_eq
