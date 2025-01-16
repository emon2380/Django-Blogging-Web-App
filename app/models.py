from django.db import models
from django.contrib.auth.models import AbstractUser

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