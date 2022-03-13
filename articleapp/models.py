from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True) # set_null은 게시글이 사라졌을 때 게시글 삭제x

    title = models.CharField(max_length=200, null=True)
    content = models.TextField(null=True)
    image = models.ImageField(upload_to='article/', null=False)

    created_at = models.DateField(auto_now_add=True, null=True)