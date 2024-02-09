from django.contrib import admin
from questions.models import Pyetje, Kategori, Progress

# Register your models here.

admin.site.register(Pyetje)
admin.site.register(Kategori)
admin.site.register(Progress)