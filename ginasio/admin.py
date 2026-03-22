from django.contrib import admin
from .models import PT, Cliente, Sessao


class PTAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    ordering = ("nome",)
    search_fields = ("nome",)


class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    ordering = ("nome",)
    search_fields = ("nome",)


class SessaoAdmin(admin.ModelAdmin):
    list_display = ("pt", "cliente", "data", "hora")
    ordering = ("data", "hora")
    search_fields = ("pt__nome", "cliente__nome")


admin.site.register(PT, PTAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Sessao, SessaoAdmin)