from rest_framework import serializers
from .models import Osoba, Stanowisko

class StanowiskoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nazwa = serializers.CharField(required=True);
    opis = serializers.CharField(required=True);

    def create(self, validate_data):
        return Stanowisko.objects.create(**validate_data)

    def update(self, instance, validated_data):
        instance.nazwa = validated_data.get('nazwa', instance.nazwa)
        instance.opis = validated_data.get('opis', instance.opis)
        instance.save()
        return instance

class OsobaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Osoba
        fields = ['id', 'imie', 'nazwisko', 'plec', 'data_dodania', 'stanowisko', 'wlasciciel']
        read_only_fields = ['id', 'wlasciciel']
        wlasciciel = serializers.ReadOnlyField(source='User.username')

    def validate_imie(self, value):
        if not value.isalpha():
            raise serializers.ValidationError(
                "Imie musi zawierac tylko litery.",
            )
        return value

    def validate_data_dodania(self, value):
        if value > datetime.now():
            raise serializers.ValidationError(
                "Data jest z przyszlosci.",
            )
        return value

    def update(self, instance, validated_data):
        instance.imie = validated_data.get('imie', instance.imie)
        instance.nazwisko = validated_data.get('nazwisko', instance.nazwisko)
        instance.plec = validated_data.get('plec', instance.plec)
        instance.stanowisko = validated_data.get('stanowisko', instance.stanowisko)
        instance.data_dodanie = validated_data.get('data_dodania', instance.data_dodania)
        instance.wlasciciel = validated_data.get('wlasciciel', instance.wlasciciel)
        instance.save()
        return instance