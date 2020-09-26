from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import pre_save
from t2t.utils import unique_slug_generator


GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
)

CATEGORY_CHOICES = (
        ('Owner', 'Owner'),
        ('Customer', 'Customer'),
        ('Admin', 'Admin'),
        ('Tenant', 'Tenant'),
)


class Account(models.Model):
    slug = models.SlugField(max_length=250, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, blank=True, null=True)
    mother_tongue = models.CharField(max_length=255)
    profile = models.ImageField(upload_to="profile_pics",blank=True, null=True)
    phone = models.CharField(max_length=15)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="customer")

    def __str__(self):
        return str(self.user)


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(slug_generator, sender=Account)
