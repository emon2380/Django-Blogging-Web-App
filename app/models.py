from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

ARTICLE_STATUS = (
    ("draft", "draft"),
    ("inprogress", "in progress"),
    ("posted", "posted"),
)

class UserProfile(AbstractUser):
    pass

class Article(models.Model):
    tittle =  models.CharField(max_length=100)
    content = models.TextField(default= '', blank=True)
    word_count = models.IntegerField(blank=True)
    twitter_post = models.TextField(default="", blank= True)
    status = models.CharField(
        max_length=20,
        choices = ARTICLE_STATUS,
        default= "draft",
        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="articles")

    def save(self, *args, **kwargs):
        # Calculate the word count based on the content
        self.word_count = len(self.content.split()) if self.content else 0
        super().save(*args, **kwargs)