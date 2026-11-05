from django.contrib import admin
from .models import Categoria, LugarPatrimonial

admin.site.register(Categoria)


class LugarAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion', 'categoria')


admin.site.register(LugarPatrimonial, LugarAdmin)
