from rest_framework import serializers
from .models import Autor, Gatunek, Book, Borrow
from django.contrib.auth.models import User
import datetime


class AutorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    imie = serializers.CharField(required=True)
    nazwisko = serializers.CharField(required=True)

    def create(self, validate_data):
        return Autor.objects.create(**validate_data)

    def validate_imie(self, value):
        if not value.isalpha():
            raise serializers.ValidationError(
                "Imie musi zawierac tylko litery.",
            )
        return value

    def update(self, instance, validated_data):
        instance.imie = validated_data.get('imie', instance.imie)
        instance.nazwisko = validated_data.get('nazwisko', instance.nazwisko)
        instance.save()
        return instance


class GatunekSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nazwa = serializers.CharField(required=True)
    opis = serializers.CharField(required=True)

    def create(self, validate_data):
        return Gatunek.objects.create(**validate_data)

    def update(self, instance, validated_data):
        instance.nazwa = validated_data.get('nazwa', instance.nazwa)
        instance.opis = validated_data.get('opis', instance.opis)
        instance.save()
        return instance


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'nazwa', 'liczba_stron', 'data_wydania', 'autor', 'gatunek']
        read_only_fields = ['id']

    def to_representation(self, instance):
        rep = super(BookSerializer, self).to_representation(instance)
        rep['autor'] = instance.autor.imie + " " + instance.autor.nazwisko
        rep['gatunek'] = instance.gatunek.nazwa
        return rep

    def validate_liczba_stron(self, value):
        if not value >= 10:
            raise serializers.ValidationError(
                "Książka jest za krótka.",
            )
        return value

    def validate_data_wydania(self, value):
        if value > datetime.now():
            raise serializers.ValidationError(
                "Data jest z przyszlosci.",
            )
        return value

    def update(self, instance, validated_data):
        instance.nazwa = validated_data.get('nazwa', instance.nazwa)
        instance.liczba_stron = validated_data.get('liczba_stron', instance.liczba_stron)
        instance.data_wydania = validated_data.get('data_wydania', instance.data_wydania)
        instance.autor = validated_data.get('autor', instance.autor)
        instance.gatunek = validated_data.get('gatunek', instance.gatunek)
        instance.save()
        return instance


class BorrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrow
        fields = ['id', 'konto', 'book', 'data_dodania', 'data_zwrotu']
        read_only_fields = ['id', 'konto']
        konto = serializers.ReadOnlyField(source='User.username')

    def to_representation(self, instance):
        rep = super(BorrowSerializer, self).to_representation(instance)
        rep['konto'] = instance.konto.username
        rep['book'] = instance.book.nazwa
        return rep

    def validate_data_dodania(self, value):
        if value > datetime.now():
            raise serializers.ValidationError(
                "Data jest z przyszlosci.",
            )
        return value

    def update(self, instance, validated_data):
        instance.konto = validated_data.get('konto', instance.konto)
        instance.book = validated_data.get('book', instance.book)
        instance.data_dodania = validated_data.get('data_dodania', instance.data_dodania)
        instance.data_zwrotu = validated_data.get('data_zwrotu', instance.data_zwrotu)
        instance.save()
        return instance
