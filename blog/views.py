from django.shortcuts import render, get_object_or_404
from .models import Article, Category, Comment
from django.core.paginator import Paginator
# Create your views here.


def post_list(request):
    articles = Article.objects.get_active_items()
    page_number = request.GET.get('page', 1)
    paginator = Paginator(articles, 2)
    objects_list = paginator.get_page(page_number)
    context = {
        'articles': objects_list
    }
    return render(request, 'blog/post_list.html', context)


def post_detail(request, slug):
    article = Article.objects.get(slug=slug)
    if request.method == "POST":
        body = request.POST.get("body")
        parent_id = request.POST.get("parent_id")
        Comment.objects.create(body=body, article=article, user=request.user, parent_id=parent_id)
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
