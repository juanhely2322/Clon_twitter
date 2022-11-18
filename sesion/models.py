from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    biografy=models.CharField(default="Hola, estoy usando twitter...",max_length=100)
    image=models.ImageField(default='default.png')
    def __str__(self):
        return f'Perfil de {self.user.username}'