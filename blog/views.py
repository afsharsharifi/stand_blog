from django.shortcuts import render
from .models import Article
# Create your views here.


def post_list(request):
    articles = Article.objects.get_active_items()
    context = {
        'articles': articles
    }
    return render(request, 'blog/post_list.html', context)


def post_detail(request, slug):
    article = Article.objects.get(slug=slug)
    context = {
        'article': article
    }
    return render(request, 'blog/post_details.html', context)
