from django.contrib import admin
from .models import Vino, Recomendacion, Preferencia

# Register your models here.
admin.site.register(Vino)
admin.site.register(Recomendacion)
admin.site.register(Preferencia)
