from django.db import models
from django.contrib.auth.models import User


class Autor(models.Model):
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=30)

    def __str__(self):
        return self.imie + " " + self.nazwisko

    class Meta:
        ordering = ["nazwisko"]
        verbose_name_plural = "Autorzy"


class Gatunek(models.Model):
    nazwa = models.CharField(max_length=20)
    opis = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name_plural = "Gatunki"


class Book(models.Model):
    nazwa = models.CharField(max_length=60)
    liczba_stron = models.PositiveIntegerField()
    data_wydania = models.DateField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    gatunek = models.ForeignKey(Gatunek, on_delete=models.CASCADE)

    def __str__(self):
        return self.nazwa


class Borrow(models.Model):
    konto = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    data_dodania = models.DateField(auto_now_add=True)
    data_zwrotu = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.konto.username + " - " + self.book.nazwa
