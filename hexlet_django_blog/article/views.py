from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class ArticleView(View):
    def index(self, request, *args, **kwargs):
        return render(request, 'article/index.html', context={'article': 'Article'})
# Create your views here.
