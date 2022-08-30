from django.shortcuts import render
from blog.models import Article
# Create your views here.


def sidebar_partial(request):
    context = {
        'name': "Afshar Sharifi",
    }
    return render(request, 'includes/sidebar.html', context)


def index_page(request):
    articles = Article.objects.get_active_items()
    context = {
        "articles": articles,
    }
    return render(request, 'home/index.html', context)
