from django.db import models
from django.utils import timezone

from users.models import Commandants, Students


# Create your models here.
class Statement(models.Model):
    title = models.CharField("Название", max_length=30)
    payment = models.BooleanField("Оплата общежития", default=False)
    status = models.CharField("Статус", max_length=30, default="Отправлено")
    date = models.DateField("Дата отправки", default=timezone.now())
    file = models.FileField("Файл заявления", upload_to="main/static/main/files", blank=True, null=True)
    student = models.ManyToManyField(Students)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Заявление"
        verbose_name_plural = "Заявления"


class Dormitory(models.Model):
    title = models.CharField("Номер", max_length=30)
    street = models.CharField("Адрес", max_length=250)
    student = models.ManyToManyField(Students)
    commandant = models.ManyToManyField(Commandants)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Общежитие"
        verbose_name_plural = "Общежития"


class VisitHistory(models.Model):
    statement = models.OneToOneField(Statement, on_delete=models.CASCADE)
    day_of_visit = models.DateField(verbose_name="Дата посещения")

    def __str__(self):
        return f"{self.statement.title} - {self.day_of_visit}"

    class Meta:
        verbose_name = "История посещения"
        verbose_name_plural = "История посещений"
