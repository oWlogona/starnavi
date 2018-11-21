from django.db import models
from django.contrib.auth.models import User

SEX_USER = (
    ('M', 'MALE'),
    ('F', 'FEMALE'),
)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(default=0)
    sex = models.CharField(max_length=25, choices=SEX_USER)

    def __str__(self):
        return self.user.username