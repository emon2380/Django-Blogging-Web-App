from app.models import Article
from django.views.generic import CreateView,ListView,DeleteView,UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models.query import QuerySet
from typing import Any

class ArticleView(LoginRequiredMixin, ListView):
    template_name = "app/home.html"
    context_object_name = "articles"
    model = Article
    def get_queryset(self) -> QuerySet[Any]:
        return Article.objects.filter(author=self.request.user)

class CreateArticleForm(LoginRequiredMixin, CreateView):
    model = Article
    fields = ["tittle", "content", "status"]
    template_name = "app/article_create.html"
    success_url = reverse_lazy("home")

class DeleteArticle(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = "app/article_delete.html"
    success_url = reverse_lazy("home")
    def test_func(self) -> bool | None:
        return self.request.user == self.get_object().author

class UpdateArticle(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ["tittle", "content", "status"]
    template_name = "app/article_update.html"
    success_url = reverse_lazy("home")
    def test_func(self) -> bool | None:
        return self.request.user == self.get_object().author