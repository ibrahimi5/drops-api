from django.db import models

# Create your models here.
class Post(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.URLField(blank=True)
    categories = models.ManyToManyField(
        to='categories.Category',
        related_name='post_categories'
    )
    owner = models.ForeignKey(
        to='users.User',
        on_delete=models.CASCADE,
        related_name='posts_owned'
    )
    likes = models.ManyToManyField(
        to='users.User',
        related_name = 'likes_by_users',
        blank = True,
    )
    comments = models.ForeignKey(
        to='comments.Comment',
        on_delete = models.DO_NOTHING,
        blank = True,
        null = True,
        related_name = 'comment'
    )


    class Meta:
        ordering = ['-created_at']  # newest to oldest

    def __str__(self):
        return self.body