from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from filmsai_rest import serializers
from filmsai_rest import models
from filmsai_rest.utils import predict # функция оценки комментария

GET_POST_METHODS = {'GET','POST'}

# Создание ViewSet для модели Film
class FilmsViewSet(viewsets.ModelViewSet):
  # Указываем базовый сериализатор для модели Film
  serializer_class = serializers.FilmBaseSerializer
  # Указываем базовый запрос к бд, определяющий начального множество объектов модели Film
  queryset = models.Film.objects.all() # Выбираем все доступные записи Film из бд
  
  # Разрешаем менять или удалять фильмы только суперпользователям
  def get_permissions(self):
    if self.request.method not in GET_POST_METHODS:
      return [IsAdminUser()]
    return super().get_permissions()

# Создание ViewSet для модели Comment
class CommentsViewSet(viewsets.ModelViewSet):
  filterset_fields = ['film', 'rating', 'assesment'] # Поля для фильтрации
  ordering_fields = ['created_at', 'rating'] # Поля для сортировки
  ordering = ['-created_at', '-rating'] # Значение сортировки по умолчанию
  # Указываем базовый сериализатор для модели Film
  serializer_class = serializers.CommentBaseSerializer
  # Указываем базовый запрос к бд, определяющий начального множество объектов модели Film
  queryset = models.Comment.objects.all() # Выбираем все доступные записи Film из бд
  
  # Переопределяем функцию, которая будет выполнена после создания/сохранения комментария
  def perform_create(self, serializer):
    comment = serializer.save() # Сохраняем комментарий и возвращаем его python объект
    predict(comment.id) # Вызываем функцию по оценки комментария
    return comment
  
  # Разрешаем менять или удалять комментарии только суперпользователям
  def get_permissions(self):
    if self.request.method not in GET_POST_METHODS:
      return [IsAdminUser()]
    return super().get_permissions()
