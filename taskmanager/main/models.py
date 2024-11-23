from django.db import models
from django.contrib.auth.models import AbstractUser

class Task(models.Model):
    title = models.CharField('Название', max_length=50)  # Исправлено на CharField
    task = models.TextField('Описание')  # Исправлено на TextField
    event_date = models.DateTimeField('Дата и время проведения')  # Дата и время
    location = models.CharField('Место проведения', max_length=100)  # Место
    image = models.ImageField('Изображение', upload_to='events/images/', null=True, blank=True)  # Поле для изображения
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2, null=True, blank=True)  # Цена


    def __str__(self):
        return f"{self.title} - {self.event_date.strftime('%d.%m.%Y %H:%M')}"

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'



class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('user', 'Пользователь'),
        ('admin', 'Администратор'),
    )
    role = models.CharField('Роль', max_length=10, choices=ROLE_CHOICES, default='user')

    # Добавляем related_name для предотвращения конфликта
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',  # Уникальное имя для связи
        blank=True
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',  # Уникальное имя для связи
        blank=True
    )

    def __str__(self):
        return self.username