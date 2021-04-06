from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.shortcuts import reverse
from django_countries.fields import CountryField
from .modules import global_parameters
from multiselectfield import MultiSelectField

CATEGORY_CHOICES = global_parameters.CATEGORY_CHOICES

LABEL_CHOICES = global_parameters.LABEL_CHOICES

ADDRESS_CHOICES = global_parameters.ADDRESS_CHOICES

ROBOT_APPLICATIONS = global_parameters.ROBOT_APPLICATIONS

AXIS_MOVEMENT = global_parameters.AXIS_MOVEMENT

MOUNTING = global_parameters.MOUNTING

DATASHEET = global_parameters.DATASHEET


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)
    one_click_purchasing = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Brand(models.Model):
    title = models.CharField(max_length=100)
    '''
    Brand infos, name, country, date, point, etc...
    '''
    def __str__(self):
        return self.title


class Controller(models.Model):
    brand = models.ForeignKey(Brand,on_delete = models.CASCADE)
    title = models.CharField(max_length=100)

    #----------------DATASHEET------------------

    def __str__(self):
        return self.title



def userprofile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        userprofile = UserProfile.objects.create(user=instance)


post_save.connect(userprofile_receiver, sender=settings.AUTH_USER_MODEL)
