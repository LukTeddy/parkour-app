from django.contrib import admin
from .models import Post, Spot, Comment, CommentMedia

# Register your models here.
admin.site.register(Post)
admin.site.register(Spot)
admin.site.register(Comment)
admin.site.register(CommentMedia)