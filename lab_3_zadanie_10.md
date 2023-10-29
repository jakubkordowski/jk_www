// import modeli
from polls.models import Osoba, Stanowisko 

// wyświetlnie wszystkich obiektów modelu osoba
Osoba.objects.all() 

// wyświetlenie obiektów modelu osoba o id=3
Osoba.objects.filter(id=3)

// wyświetlenie obiektów modelu osoba, które zaczynają się K
Osoba.objects.filter(imie__startswith='K')

//wyświetlanie unikalnych stanowisk
Osoba.objects.order_by().values('stanowisko').distinct()

// wyświetlanie stanowisk posortowanych alfabetycznie malejąco
Stanowisko.objects.order_by('-nazwa')

// dodanie osoby
osoba4 = Osoba(imie="Alan", nazwisko="Alanowski", plec="2", stanowisko=Stanowisko.obkects.get(id=1))
osoba4.save()