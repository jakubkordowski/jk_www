import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Stanowisko(models.Model):
    nazwa = models.CharField(max_length=200)
    opis = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name_plural = "stanowiska"

class Osoba(models.Model):
    class plec(models.IntegerChoices):
        KOBIETA = 1
        MEZCZYZNA = 2
        INNE = 3
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=30)
    plec = models.IntegerField(choices=plec.choices, default=plec.INNE)
    stanowisko = models.ForeignKey(Stanowisko, on_delete=models.CASCADE)
    data_dodania = models.DateField(auto_now_add=True)
    wlasciciel = models.ForeignKey(User, related_name='Osoba', on_delete=models.CASCADE)

    def __str__(self):
        return self.imie + " " + self.nazwisko

    class Meta:
        ordering = ["nazwisko"]
        verbose_name_plural = "osoby"

