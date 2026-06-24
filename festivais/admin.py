from django.contrib import admin

from .models import Artista, Festival, Palco


class PalcoInline(admin.TabularInline):
    model = Palco
    extra = 1


@admin.register(Artista)
class ArtistaAdmin(admin.ModelAdmin):
    list_display = ("nome", "genero")
    ordering = ("nome",)
    search_fields = ("nome", "genero")
    list_filter = ("genero",)


@admin.register(Festival)
class FestivalAdmin(admin.ModelAdmin):
    list_display = ("nome", "local", "data_inicio", "data_fim")
    ordering = ("data_inicio", "nome")
    search_fields = ("nome", "local", "artistas__nome")
    list_filter = ("data_inicio", "local")
    filter_horizontal = ("artistas",)
    inlines = (PalcoInline,)


@admin.register(Palco)
class PalcoAdmin(admin.ModelAdmin):
    list_display = ("nome", "festival")
    ordering = ("festival__nome", "nome")
    search_fields = ("nome", "festival__nome")
    list_filter = ("festival",)

