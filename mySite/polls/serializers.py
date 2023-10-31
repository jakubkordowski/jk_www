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
        fields = ['id', 'imie', 'nazwisko', 'plec', 'data_dodania', 'stanowisko']
        read_only_fields = ['id']