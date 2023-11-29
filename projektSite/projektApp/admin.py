from django.contrib import admin

from .models import Autor, Gatunek, Book, Borrow


@admin.display(description="Autor (ID)")
def autor_id(obj):
    return f"{obj.autor.imie} {obj.autor.nazwisko} ({obj.autor.id})"


@admin.register(Book)
class BookDataAdmin(admin.ModelAdmin):
    list_display = ("nazwa", autor_id,)
    list_filter = ("autor", "gatunek",)


@admin.register(Autor)
class AutorDataAdmin(admin.ModelAdmin):
    list_display = ("nazwisko", "imie", )


@admin.register(Gatunek)
class GatunekDataAdmin(admin.ModelAdmin):
    list_display = ("nazwa", )


@admin.register(Borrow)
class BorrowDataAdmin(admin.ModelAdmin):
    list_display = ("konto", "book", "data_dodania", "data_zwrotu",)
