from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Notification(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_notifications', )
    subject = models.CharField(max_length=50, )
    message = models.TextField()
    participants = models.ManyToManyField(User, related_name='notifications', )
    send_at = models.DateTimeField()

    def __str__(self):
        return self.title
