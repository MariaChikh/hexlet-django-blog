from django.urls import path

from hexlet_django_blog.article import views
from .views import ArticleView

urlpatterns = [
    path('<str:tags>/<int:article_id>/', ArticleView.as_view(), name="article"),
]
