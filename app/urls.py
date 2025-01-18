from django.urls import path
from app.views import ArticleView, CreateArticleForm, DeleteArticle, UpdateArticle

urlpatterns = [
    path("",ArticleView.as_view(),name="home"),
    path("create/", CreateArticleForm.as_view(),name="create_article"),
    path("<int:pk>/update", UpdateArticle.as_view(), name="update_article"),
    path("<int:pk>/delete", DeleteArticle.as_view(), name="delete_article"),
]