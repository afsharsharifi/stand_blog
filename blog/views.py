from django.shortcuts import render
from .models import Article
# Create your views here.


def post_detail(request, id):
    article = Article.objects.get(id=id)
    context = {
        'article': article
    }
    return render(request, 'blog/post_details.html', context)
