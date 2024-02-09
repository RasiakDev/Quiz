from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Kategori(models.Model):
    kategoria=models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.kategoria

class Pyetje(models.Model):
    question = models.TextField()
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100, blank=True, null=True)
    option4 = models.CharField(max_length=100, blank=True, null=True)
    correct = models.CharField(max_length=100)
    category = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
       verbose_name_plural = "Pyetjet"

    def __str__(self) -> str:
        return self.question


class Progress(models.Model):
    category = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    question = models.ForeignKey(Pyetje, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

