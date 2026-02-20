from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.sender} -> {self.receiver}"
