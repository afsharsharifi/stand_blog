from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import ListView, DetailView
import time

from .models import Article, Category, Comment

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


def search_posts(request):
    q = request.GET.get("q")
    articles = Article.objects.filter(title__icontains=q)
    page_number = request.GET.get('page', 1)
    paginator = Paginator(articles, 2)
    objects_list = paginator.get_page(page_number)
    context = {
        'articles': objects_list
    }
    return render(request, 'blog/post_list.html', context)


class ArticleList(ListView):
    model = Article
    context_object_name = "articles"
    paginate_by = 2
    queryset = Article.objects.get_active_items()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "Afshar Sharifi"
        context["page"] = context["page_obj"]
        return context


class ArticleDetail(DetailView):
    model = Article
    template_name = "blog/article_detail.html"  # lower_model_name + _detail
    context_object_name = "article"  # lower_model_name
    slug_field = "slug"  # slug
    slug_url_kwarg = "slug"  # slug
    queryset = Article.objects.get_active_items()  # model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "Afshar Sharifi"
        return context


class HomePageRedirect(RedirectView):
    pattern_name = "blog:post_list"
    permanent = False
    query_string = False

    def get_redirect_url(self, *args, **kwargs):
        for i in range(10):
            print(i)
            time.sleep(1)
        return super().get_redirect_url(*args, **kwargs)
