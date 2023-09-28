from django.contrib.auth.models import AbstractUser
from django.db import models


class GenderType(models.IntegerChoices):
    MALE = 1
    FEMALE = 2


class User(AbstractUser):
    """Пользователь."""

    register_date = models.DateField(verbose_name='Дата регистрации', auto_now_add=True)
    gender = models.IntegerField(choices=GenderType.choices, verbose_name='Пол')
    dob = models.DateField(blank=True, null=True, verbose_name='Дата рождения')

    class Meta(AbstractUser.Meta):
        ordering = ('username',)

    @property
    def full_name(self):
        return self.get_full_name()
