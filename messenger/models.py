from django.db import models
from django.conf import settings


class Profile(models.Model):
    """
    Profile Model: Holds information about the user Profile
    """

    FEMALE = 0
    MALE = 1
    OTHER = 2

    GENDER_CHOICES = (
        (FEMALE, 'Femenino'),
        (MALE, 'Masculino'),
        (OTHER, 'Otro')
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    gender = models.PositiveSmallIntegerField(
        choices=GENDER_CHOICES, default=OTHER)
    bio = models.TextField(null=True, blank=True)
    onesignal_playerId = models.CharField(
        max_length=500, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user
