from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Spot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name

class Comment(models.Model):
    spot = models.ForeignKey(Spot, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    text = models.TextField()
    is_challenge = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.spot.name}'

    class Meta:
        ordering = ['-created_at']

class CommentMedia(models.Model):
    comment = models.ForeignKey(Comment, related_name="media", on_delete=models.CASCADE)
    media_file = models.FileField(upload_to='comments/')
    media_type = models.CharField(max_length=10, choices=[('image', "Image"), ('video', 'Video')])

    def __str__(self):
        return f'Media for comment {self.comment.id}'
