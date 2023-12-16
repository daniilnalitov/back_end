from django.contrib import admin
from filmsai_rest import models

# Объевление классов админских панелей
class FilmAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass

# Добавление на страницу администратора моделей и их админских панелей
admin.site.register(models.Film, FilmAdmin)
admin.site.register(models.Comment, CommentAdmin)