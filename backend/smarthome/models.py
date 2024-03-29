from django.db import models


# Create your models here.
class HomeStatus(models.Model):
    class Meta:
        verbose_name_plural = "Home Statuses"

    on = models.BooleanField()
    sent_at = models.DateTimeField()
    recieved_at = models.DateTimeField(auto_now_add=True)
