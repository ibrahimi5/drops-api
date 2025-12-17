from django.db import models

# Create your models here.
class Comment(models.Model):
    text = models.TextField()
    date = models.DateTimeField()
    owner = models.ForeignKey(
        to='users.User',
        on_delete=models.CASCADE,
        related_name='comments_owned'
    ) 