from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        tags = 'python'
        article_id = 42
        url = reverse('article', kwargs={'tags':tags, 'article_id': article_id})
        return redirect(url)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'World'
        return context

def about(request):
    tags = ['обучение', 'программирование', 'Python', 'oop']
    return render(request, 'about.html', context={'tags': tags})