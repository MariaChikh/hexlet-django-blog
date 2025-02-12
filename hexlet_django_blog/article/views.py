from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class ArticleView(View):
    def get(self, request, tags, article_id, *args, **kwargs):
        context = {
            'article_id': article_id,
            'tags': tags,
        }
        return render(request, 'article/index.html', context)
    
    
# Create your views here.
