from django.db import models

# Create your models here.

class Career(models.Model):
    role = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    comnpany = models.CharField(max_length=100)

    def __str__(self):
        return self.role

