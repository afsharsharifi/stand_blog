from django.shortcuts import render, get_object_or_404
from .models import Article, Category
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


def category_detail(request, pk):
    category = get_object_or_404(Category, id=pk)
    articles = category.articles.get_active_items()
    context = {
        'articles': articles
    }
    return render(request, 'blog/post_list.html', context)
