from django.contrib.auth.models import AbstractUser, Group
from django.db import models


# Create your models here.
class User(AbstractUser):
    pass


class Students(models.Model):
    first_name = models.CharField("Имя", max_length=40)
    last_name = models.CharField("Фамилия", max_length=40)
    room = models.CharField("Комната", max_length=40, default="")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Студенты"
        verbose_name_plural = "Студенты"


class Commandants(models.Model):
    first_name = models.CharField("Имя", max_length=40)
    last_name = models.CharField("Фамилия", max_length=40)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Комендант"
        verbose_name_plural = "Коменданты"
