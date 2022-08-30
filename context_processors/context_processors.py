from blog.models import Article, Category


def recent_articles(request):
    recent_articles = Article.objects.get_active_items().order_by("-created")[:3]
    return {"recent_articles": recent_articles, }


def article_categories(request):
    categories = Category.objects.all()
    return {"categories": categories, }
