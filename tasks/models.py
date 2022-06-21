from telnetlib import STATUS
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


class Task(models.Model):

    STATUS = (
        ('doing', 'Aberto'),
        ('done', 'Fechado'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    done = models.CharField(
        max_length=5,
        choices=STATUS,
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
