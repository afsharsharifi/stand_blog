from django.shortcuts import render, redirect
from blog.models import Article
from .models import Message
from home.forms import ContactUsForm
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


def contact_us(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.title += " Added"
            instance.save()
    else:
        form = ContactUsForm()

    context = {
        'form': form
    }
    return render(request, 'home/contact.html', context)
