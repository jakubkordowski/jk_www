from django.contrib import admin

from .models import Question, Stanowisko, Osoba

admin.site.register(Question)

@admin.display(description="Stanowisko (ID)")
def stan_id(obj):
    return f"{obj.stanowisko.nazwa} ({obj.stanowisko.id})"

@admin.register(Osoba)
class OsobaDataAdmin(admin.ModelAdmin):
    readonly_fields = ('data_dodania',)
    list_display = ("imie", "nazwisko", stan_id,)
    list_filter = ("stanowisko", "data_dodania",)

@admin.register(Stanowisko)
class StanowiskoDataAdmin(admin.ModelAdmin):
    list_filter = ("nazwa",)
