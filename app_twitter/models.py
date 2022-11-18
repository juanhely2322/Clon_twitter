from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class post(models.Model):
    timestamp=models.DateTimeField(default=timezone.now)
    content=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="posts")

    class Meta:
        ordering=['-timestamp']
        
    def __self__(self):
        return self.content