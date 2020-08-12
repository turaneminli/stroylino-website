from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.conf import settings

from users.models import CustomUser

from PIL import Image

from django.db.models.signals import pre_save, post_save


# Create your models here.
User = get_user_model()
class Post(models.Model):

    title = models.CharField(max_length=28)
    image = models.FileField(null=True, blank=True, upload_to='static/media/')
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=True,
        blank=False,
    )
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     img = Image.open(self.image.path)

    #     if img.height > 500 or img.weight > 300:
    #         output_size = (500, 500)
    #         img.thubnail(output_size)
    #         img.save(self.image.path)

class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('home')

class CommentNotification(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
    )
    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        related_name='notifications',
    )
    read = models.BooleanField(default=False)
    

