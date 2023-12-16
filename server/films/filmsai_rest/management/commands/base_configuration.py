# базовый класс для всех Django команд
from django.core.management.base import BaseCommand
# модель пользователя, используемого для авторизации в Django
from django.contrib.auth.models import User

# класс пользовательской команды
class Command(BaseCommand):
  # текст подсказки для команды
  help = 'default superuser creating command'
  
  # основная функцию для описания логики команды
  def handle(self, *args, **options):
    try:
      # проверяем на наличие базового суперпользователя
      User.objects.get(username='admin')
      self.stdout.write(self.style.SUCCESS('base superuser already exists'))
    except:
      # создаем суперпользователя, если его нет в базе данных
      User.objects.create_superuser(username='admin', password='admin')
      self.stdout.write(self.style.SUCCESS('creating superuser'))