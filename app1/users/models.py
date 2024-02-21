from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    image = models.ImageField(upload_to='users_image', blank = True, null = True, verbose_name='Avatar')
    class Meta:
        db_table = 'user'
        verbose_name= 'Користувача'
        verbose_name_plural = 'Користувачі'

    def __str__(self):
        return self.username