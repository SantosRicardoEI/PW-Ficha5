from django.contrib import admin
from .models import Ingrediente, Receita


class IngredienteAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    ordering = ("nome",)
    search_fields = ("nome",)


class ReceitaAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    ordering = ("nome",)
    search_fields = ("nome",)
    filter_horizontal = ("ingredientes", "favoritas")


admin.site.register(Ingrediente, IngredienteAdmin)
admin.site.register(Receita, ReceitaAdmin)