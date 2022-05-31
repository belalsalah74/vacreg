from django.db import models
from datetime import datetime,timedelta
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from cities import CITY_CHOICES

User = settings.AUTH_USER_MODEL

class Vaccine(models.Model):
   
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class VaccineShot(models.Model):

    STATUS_CHOICES = (
        ('P', 'Pending'),
        ('C', 'Completed'), 
        ('F', 'Failed'), 
    )

    vaccine = models.OneToOneField(Vaccine,on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, default='P')
    register_date = models.DateField(auto_now_add=True)
    shot_date = models.DateField(blank=True, null=True)
   

@receiver(post_save,sender=VaccineShot)
def shot_date(instance,created,*args, **kwargs):
    if created:
        shot_date = f'{instance.register_date + timedelta(days=30)}'
        instance.shot_date = shot_date
        instance.save()
