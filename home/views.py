from django.shortcuts import render
from blog.models import Article
# Create your views here.


def index_page(request):
    articles = Article.objects.get_active_items()
    recent_articles = Article.objects.get_active_items().order_by("-created")[:3]
    context = {
        "articles": articles,
        "recent_articles": recent_articles,
    }
    return render(request, 'home/index.html', context)
