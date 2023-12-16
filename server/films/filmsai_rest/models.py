from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Film(models.Model):
    # Заголовок фильма
    title = models.CharField(
        max_length=512 # Максимальное кол-во символов в названии
    )
    # Описание фильма
    description = models.TextField()
    # Постер фильма
    image = models.FileField()
    # Дата публикации фильма
    pub_date = models.DateField()
    
    # Магическая функция для красивого вывода моделей в админской панели
    def __str__(self) -> str:
        return f"<Film: {self.pk=} {self.title=}>"


class Comment(models.Model):
    # Отношение o2m к модели Film
    film = models.ForeignKey(
        Film, # Класс модели для которой будет построен FOREIGN KEY
        on_delete=models.CASCADE, # тип действия при удалении модели
        related_name='comments' # поле, через которое можно обратиться к объектам Comment из модели Film
    )
    # Дата создания комментария
    created_at = models.DateTimeField(
        auto_now=True # Устанавливаем, чтоб БД самостоятельно задавало время создания при записи модели
    )
    # Ник пользователя, создавшего комментарий
    username = models.CharField(
        max_length=64 # Максимальное кол-во символов в имени пользователя
    )
    # Содержание комментария
    comment = models.TextField()
    # Рейтинг комментария от 1 до 10
    rating = models.IntegerField(
        validators=[ # список проверок перед сохранению модели
            MinValueValidator(1), # минимальное значение должно быть не меньше 1
            MaxValueValidator(10) # максимальное значение должно быть не больше 10
        ],
        default=None, # значение по умолчанию (в БД null)
        null=True, # устанавливаем, что поле может принимать null
    )
    # Оценка комментария (Положительный или отрицательный)
    assesment = models.BooleanField(
        default=None, # значение по умолчанию (в БД null)
        null=True, # устанавливаем, что поле может принимать null
    )
    # Магическая функция для красивого вывода моделей в админской панели
    def __str__(self) -> str:
        return f"<Comment: {self.pk=} {self.assesment=} {self.rating=}>"

