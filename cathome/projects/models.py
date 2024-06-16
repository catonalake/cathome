from django.db import models
from datetime import datetime

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=120)
    customer = models.CharField(max_length=120)
    date_added = models.DateTimeField(auto_now=datetime.now())

    @property
    def special_client(self):
        if self.customer in ["Shani", "Carver"]:
            return 'special'
        return None