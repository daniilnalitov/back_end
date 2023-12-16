from filmsai_rest import models
import random

# Функция для вызова моделей
def predict(comment_id: int) -> None:
    # comment - объект комментария в базе данных, который будет изменен
    comment = models.Comment.objects.get(id=comment_id)

    # Код для обновления полей комментария
    comment.rating = random.randint(0,10)
    comment.assesment = random.random() > .5
    # Сохранение обновленного объекта в базу данных
    comment.save()