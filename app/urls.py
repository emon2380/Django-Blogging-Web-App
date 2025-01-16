from django.urls import path
from app.views import home, create_article

urlpatterns = [
    path("",home,name="home"),
    path("article/create/", create_article,name="create_article")
]