from polls.models import Osoba

from polls.models import Stanowisko

from polls.serializers import OsobaSerializer

from polls.serializers import StanowiskoSerializer

from rest_framework.renderers import JSONRenderer

from rest_framework.parsers import JSONParser

osoba = Osoba(imie="Konrad", nazwisko="Konradowski", plec="2", stanowisko=Stanowisko.objects.get(id=1))

osoba.save()

serializer = OsobaSerializer(osoba)

serializer.data

content = JSONRenderer().render(serializer.data)

content

stanowisko = Stanowisko(nazwa="Grafik", opis="osoba estetyczna")

stanowisko.save()

serializer = StanowiskoSerializer(stanowisko)

serializer.data

content = JSONRenderer().render(serializer.data)

content