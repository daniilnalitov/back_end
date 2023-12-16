from rest_framework import serializers
from filmsai_rest import models

# Сериализатор для модели Film
class FilmBaseSerializer(serializers.ModelSerializer):
    
    class Meta:
        # Указываем для какой модели бд создается сериализатор
        model = models.Film
        # Определяем какие поля модели бд использовать
        fields = '__all__' # используем все поля модели
        
# Сериализатор для модели Comment
class CommentBaseSerializer(serializers.ModelSerializer):
    
    class Meta:
        # Указываем для какой модели бд создается сериализатор
        model = models.Comment
        # Определяем какие поля модели бд использовать
        fields = '__all__' # используем все поля модели
        # Перечисляем поля, которые будут использованы только для чтения
        read_only_fields = ('rating', 'assesment')