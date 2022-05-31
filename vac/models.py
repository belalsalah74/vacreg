from django.db import models

from django.conf import settings
User = settings.AUTH_USER_MODEL

class Vaccine(models.Model):
    STATUS_CHOICES = (
        ('P','Pending'),
        ('C','Completed')
    )


    name = models.CharField(max_length=255)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    status = models.CharField(max_length=1,choices=STATUS_CHOICES,default='P')
    date = models.DateTimeField()