from django.db import models

# Create your models here.



class PageVisit(models.Model):
    # id -> primary key
    path = models.TextField(null=True, blank=True)
    taimestamp = models.DateTimeField(auto_now_add=True)
