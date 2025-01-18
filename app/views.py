from app.models import Article
from django.views.generic import CreateView,ListView,DeleteView,UpdateView
from django.urls import reverse_lazy

class ArticleView(ListView):
    template_name = "app/home.html"
    context_object_name = "articles"
    model = Article

class CreateArticleForm(CreateView):
    model = Article
    fields = ["tittle", "content", "status"]
    template_name = "app/article_create.html"
    success_url = reverse_lazy("home")

class DeleteArticle(DeleteView):
    model = Article
    template_name = "app/article_delete.html"
    success_url = reverse_lazy("home")

class UpdateArticle(UpdateView):
    model = Article
    fields = ["tittle", "content", "status"]
    template_name = "app/article_update.html"
    success_url = reverse_lazy("home")